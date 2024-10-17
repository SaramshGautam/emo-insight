# Emo-Insight Application

**Emo-Insight** is a journal-driven emotional analysis application. The app takes user journal inputs, predicts their emotional state based on the text, keeps track of these emotions over time, and suggests exercises to improve mental well-being based on the journal content.

## Features

- **Journal Input:** Users can submit their journal entries, which are analyzed to predict their emotional state.
- **Emotional Tracking:** The app tracks the user's emotions over time, providing insights through visual charts.
- **Exercise Suggestions:** Based on the journal input, the app generates mental health exercises, suggested using OpenAI's GPT API.

## Getting Started

Follow the steps below to set up both the backend (Python) and frontend (React) components of the Emo-Insight application.

### 1. Clone the Repository
```bash
git clone <your-repository-url>
```

### 2. Backend Setup

The backend handles emotion prediction and exercise suggestions using the GPT model.

#### Step 1: Navigate to the `backend` folder
```bash
cd backend
```

#### Step 2: Set up a Python Virtual Environment
Create and activate a virtual environment:

- For macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- For Windows:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

#### Step 3: Install Requirements
Install the necessary Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### Step 4: Set up the OpenAI API Key
Create a `.env` file in the `backend` folder and add your OpenAI API key:
```
OPENAI_API_KEY=<YOUR_API_KEY>
```

#### Step 5: Run the Backend Server
Start the Python backend:
```bash
python3 emotion-server.py
```

### 3. Frontend Setup

The frontend is a React application that allows users to input their journal and view emotional tracking and exercise suggestions.

#### Step 1: Navigate to the `journal` folder
```bash
cd ../journal
```

#### Step 2: Install Frontend Dependencies
```bash
npm install
```

#### Step 3: Start the Frontend Application
```bash
npm start
```

The frontend will be running on `http://localhost:3000`.

### 4. OpenAI API Setup
The exercise suggestions feature uses OpenAI's GPT model. To use this feature, follow these steps:

1. Go to the [OpenAI API](https://platform.openai.com/) and subscribe.
2. Get your API key from your OpenAI account.
3. Add the API key to your `.env` file located in the `backend` folder:
   ```
   OPENAI_API_KEY=<YOUR_API_KEY>
   ```

## Folder Structure

```
emo-insight/
│
├── backend/                    # Backend code
│   ├── emotion-server.py        # Main Flask server for emotion and exercise prediction
│   ├── requirements.txt         # Python dependencies
│   └── venv/                    # Virtual environment (not pushed to Git)
│
├── journal/                     # Frontend code (React app)
│   ├── node_modules/            # Node.js dependencies
│   ├── public/                  # Public assets
│   ├── src/                     # React source code
│   ├── package.json             # NPM dependencies and scripts
│   ├── package-lock.json        # NPM lock file
│   └── README.md                # Frontend readme
│
└── .env                         # Environment variables for API keys
```

## API Overview

### Emotion Prediction Endpoint

- **Endpoint:** `/predict-emotion`
- **Method:** `POST`
- **Description:** Accepts journal text input and returns the predicted emotional state of the user.
- **Request Body:**
  ```json
  {
    "paragraph": "Your journal entry here"
  }
  ```

- **Response:**
  ```json
  {
    "overall_emotion": "happy",
    "sentence_emotions": [
      {"sentence": "I feel great.", "emotion": "happy"},
      {"sentence": "I am stressed.", "emotion": "anxious"}
    ]
  }
  ```

### Exercise Suggestion Endpoint

- **Endpoint:** `/suggest-exercise`
- **Method:** `POST`
- **Description:** Generates mental health exercises based on the journal input.
- **Request Body:**
  ```json
  {
    "journal": "Your journal entry here"
  }
  ```

- **Response:**
  ```json
  {
    "exercise": "<Formatted exercise suggestions>"
  }
  ```

## License

This project is open-source. Feel free to modify and contribute as needed.

---

By following these steps, you can run Emo-Insight locally, track your emotions, and get personalized mental health exercises based on your journal entries.
