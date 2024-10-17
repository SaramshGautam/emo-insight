from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import nltk
from collections import Counter
import openai
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Add CORS configuration to allow the specific origin (React app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3001"}})

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the emotion detection pipeline using PyTorch weights
pipe = pipeline("text2text-generation", model="mrm8488/t5-base-finetuned-emotion")

# Define a mapping from predicted emotions to the 4 main states
emotion_mapping = {
    "joy": "happy",      
    "love": "happy",     
    "sadness": "sad",    
    "fear": "anxious",   
    "surprise": "confused",
    "anger": "angry"
}

# Function to get emotion for a given text
def get_emotion(text):
    result = pipe(text)[0]['generated_text'].strip()  # Extract the 'generated_text' from pipeline output
    
    # Map the result to one of the main states
    main_emotion = emotion_mapping.get(result, "confused")  # Default to 'confused' if emotion not mapped
    return main_emotion

@app.route('/predict-emotion', methods=['POST'])
def analyze_paragraph():
    data = request.get_json()  # Get the JSON payload from the client
    paragraph = data.get("paragraph", "")  # Extract the 'paragraph' field from the request
    
    # Log the input text (for debugging)
    print(f"Received paragraph: {paragraph}")
    
    # Tokenize the paragraph into sentences
    sentences = nltk.sent_tokenize(paragraph)
    emotions = []

    # Get emotion for each sentence and log it
    for sentence in sentences:
        emotion = get_emotion(sentence)
        emotions.append({"sentence": sentence, "emotion": emotion})
        print(f"Sentence: {sentence} -> Emotion: {emotion}")

    # Determine the overall emotion based on the most common emotion and log it
    all_emotions = [e["emotion"] for e in emotions]
    overall_emotion = Counter(all_emotions).most_common(1)[0][0]
    print(f"Overall Emotion: {overall_emotion}")
    
    # Return all sentence predictions and the overall emotion
    return jsonify({
        "overall_emotion": overall_emotion,
        "sentence_emotions": emotions  # List of sentence-level emotions
    })

@app.route('/suggest-exercise', methods=['POST'])
def exercise():
    try:
        data = request.get_json()
        journal_text = data.get('journal', '')

        # Prepare message for GPT model
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": (
                    f"Generate a set of 3 exercises that would help the mental health "
                    f"of a person whose journal entry includes:\n\n{journal_text}. "
                    "The exercises should be concise yet meaningful. Format the exercises "
                    "using bullet points and headers for clarity. Use the following structure:\n\n"
                    "- Start each exercise with a header.\n"
                    "- Provide a short objective in a single sentence.\n"
                    "- Give step-by-step instructions in bullet points."
                    "\nStrictly do not include any markdown formattings but use html tags instead."
                )
            }
        ]

        # Send request to OpenAI GPT API
        response = openai.chat.completions.create(
            model="gpt-4o",  
            messages=messages,
            max_tokens=500,  
            temperature=0.5,
        )

        final_exercise = response.choices[0].message.content
        print("--- Exercise suggestion ---: \n", final_exercise)

        return jsonify({'exercise': final_exercise}), 200

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({'error': 'Error occurred during exercise suggestion'}), 500




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)