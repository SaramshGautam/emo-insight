import click
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from transformers import pipeline
import nltk
from collections import Counter
import openai
from dotenv import load_dotenv
import sys
import os
import json
from db import db

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from models.emo_insights import EmoInsights

app = Flask(__name__)
app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))  # Get the absolute path to the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "../database/emo-db.db")}'

db.init_app(app)
migrate = Migrate(app, db)


CORS(app, resources={r"/*": {"origins": "*"}})

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

pipe = pipeline("text2text-generation", model="mrm8488/t5-base-finetuned-emotion")

# Mapping from predicted emotions to the 5 main states
emotion_mapping = {
    "joy": "happy",      
    "love": "happy",     
    "sadness": "sad",    
    "fear": "anxious",   
    "surprise": "confused",
    "anger": "angry"
}

@app.cli.command("drop-db")
def drop_db():
    try:
        with app.app_context():
            db.drop_all()
            print("Database tables dropped successfully.")
    except Exception as e:
        print(f"Error dropping the database: {e}")

@app.cli.command("create-db")
def create_db():
    try:
        with app.app_context():
            db.create_all()
            print("Database tables created.")
    except Exception as e:
        print(f"Error creating the database: {e}")

@app.cli.command("seed-db")
def seed_db():
    try:
        seed_data = [
            {
                "date": "2024-09-01",
                "happy": 70,
                "sad": 30,
                "angry": 20,
                "anxious": 50,
                "confused": 10
            },
            {
                "date": "2024-09-02",
                "happy": 60,
                "sad": 40,
                "angry": 10,
                "anxious": 30,
                "confused": 50
            },
            {
                "date": "2024-09-03",
                "happy": 60,
                "sad": 20,
                "angry": 10,
                "anxious": 20,
                "confused": 5
            },
            {
                "date": "2024-09-04",
                "happy": 20,
                "sad": 70,
                "angry": 20,
                "anxious": 30,
                "confused": 10
            },
            {
                "date": "2024-09-05",
                "happy": 15,
                "sad": 5,
                "angry": 15,
                "anxious": 35,
                "confused": 45
            },
            {
                "date": "2024-09-06",
                "happy": 60,
                "sad": 40,
                "angry": 10,
                "anxious": 30,
                "confused": 50
            },
            {
                "date": "2024-09-07",
                "happy": 25,
                "sad": 10,
                "angry": 50,
                "anxious": 20,
                "confused": 10
            },
            {
                "date": "2024-09-08",
                "happy": 10,
                "sad": 20,
                "angry": 10,
                "anxious": 35,
                "confused": 10
            },
            {
                "date": "2024-09-10",
                "happy": 15,
                "sad": 25,
                "angry": 20,
                "anxious": 30,
                "confused": 50
            },
            {
                "date": "2024-09-11",
                "happy": 45,
                "sad": 45,
                "angry": 20,
                "anxious": 35,
                "confused": 35
            }
        ]

        with app.app_context():
            # Insert data into EmoInsights table
            for data in seed_data:
                new_insight = EmoInsights(
                    happy=data["happy"],
                    sad=data["sad"],
                    angry=data["angry"],
                    anxious=data["anxious"],
                    confused=data["confused"],
                    created_at=datetime.strptime(data["date"], "%Y-%m-%d")
                )
                db.session.add(new_insight)

            # Add the data to the session
            db.session.commit()

            print("Database seeded successfully.")
    except Exception as e:
        print(f"Error seeding the database: {e}")

# Function to get emotion for a given text
def get_emotion(text):
    result = pipe(text)[0]['generated_text'].strip()  
    
    main_emotion = emotion_mapping.get(result, "confused")  # Default to 'confused' if emotion not mapped
    return main_emotion

@app.route('/emotions-history', methods=['GET'])
def get_emotions_history():
    try:
        # Fetch all EmoInsights records, ordered by created_at
        insights = EmoInsights.query.order_by(EmoInsights.created_at).all()

        # Format the results into the desired JSON structure
        emotions_history = []
        for insight in insights:
            # Format the created_at field to just the date part
            formatted_date = insight.created_at.strftime('%Y-%m-%d')
            emotions_history.append({
                "date": formatted_date,
                "happy": insight.happy,
                "sad": insight.sad,
                "angry": insight.angry,
                "anxious": insight.anxious,
                "confused": insight.confused
            })

        return jsonify(emotions_history), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve data'}), 500

# @app.route('/emotions-history', methods=['GET'])
# def get_emotions_history():
#     try:
#         with open('./data/emotions_history.json', 'r') as file:
#             history_data = json.load(file)
#         return jsonify(history_data), 200
#     except Exception as e:
#         return jsonify({'error': 'Failed to retrieve data'}), 500

# Helper function
def map_emotions_to_levels(emotions):
    levels = {"happy": 0, "sad": 0, "angry": 0, "anxious": 0, "confused": 0}
    emotion_counts = {}

    # Count occurrences of each emotion
    for emotion in emotions:
        if emotion in emotion_counts:
            emotion_counts[emotion] += 1
        else:
            emotion_counts[emotion] = 1

    # Calculate percentage levels for each emotion
    total_sentences = len(emotions)
    levels["happy"] = int((emotion_counts.get("happy", 0) / total_sentences) * 100)
    levels["sad"] = int((emotion_counts.get("sad", 0) / total_sentences) * 100)
    levels["angry"] = int((emotion_counts.get("angry", 0) / total_sentences) * 100)
    levels["anxious"] = int((emotion_counts.get("anxious", 0) / total_sentences) * 100)
    levels["confused"] = int((emotion_counts.get("confused", 0) / total_sentences) * 100)

    return levels

def create_emo_insight(emotions):
    data = map_emotions_to_levels(
        [item['emotion'] for item in emotions]
    )

    new_insight = EmoInsights(
        happy=data['happy'],
        sad=data['sad'],
        angry=data['angry'],
        anxious=data['anxious'],
        confused=data['confused']
    )
    db.session.add(new_insight)
    db.session.commit()

    return new_insight.to_dict()

@app.route('/predict-emotion', methods=['POST'])
def analyze_paragraph():
    data = request.get_json()  
    paragraph = data.get("paragraph", "")  
    
    print(f"Received paragraph: {paragraph}")
    
    sentences = nltk.sent_tokenize(paragraph)
    emotions = []

    for sentence in sentences:
        emotion = get_emotion(sentence)
        emotions.append({"sentence": sentence, "emotion": emotion})
        print(f"Sentence: {sentence} -> Emotion: {emotion}")

    all_emotions = [e["emotion"] for e in emotions]
    overall_emotion = Counter(all_emotions).most_common(1)[0][0]

    # Extracting and saving emotions stats
    emotions_stat = create_emo_insight(emotions)

    print(f"Overall Emotion: {overall_emotion}")

    return jsonify({
        "overall_emotion": overall_emotion,
        "sentence_emotions": emotions_stat
    })

@app.route('/suggest-exercise', methods=['POST'])
def exercise():
    try:
        data = request.get_json()
        journal_text = data.get('journal', '')

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
    app.run(debug=True, host='0.0.0.0', port=8000)
