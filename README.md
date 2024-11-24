# Emo-Insight

Emo-Insight is an application that analyzes the emotional state of users based on their journal entries. It predicts emotions from the journal content and provides exercise suggestions for mental well-being. The application has a Python Flask backend for emotion prediction and a React frontend for user interactions.

## Project Structure

- **backend**: Contains the Python Flask server for processing journal entries and predicting emotions.
- **journal**: Contains the React frontend for user input, visualization, and interaction with the app.

## Getting Started

### Prerequisites

- **Git**: To clone the repository
- **Python 3**: For the backend server
- **Node.js and npm**: For the frontend React application

### Cloning the Repository

```bash
git clone https://github.com/SaramshGautam/emo-insight.git
cd emo-insight
```

# Backend Setup (Python Flask)

## Steps

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a Python virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

On Linux/macOS:
```bash

source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Download NLTK dependencies:

```bash
python
>>> import nltk
>>> nltk.download('punkt')
>>> exit()
```

6. Run the backend server (using flask). `cd` into the backend directory and run:

```bash
flask --app emotion-server.py run
```

7. Create a new window of terminal, again source into venv following the STEP 3 and `cd` into database directory. Run the following:

```bash
export FLASK_APP=emotion-server
flask create-db
flask seed-db
```

**Note:** Step 7 needs to be run only once for setting up the database.


# Frontend Setup (React)

1. Navigate to the frontend directory:

```bash
cd journal
```

2. Install dependencies:

```bash
npm install
```

3. Start the frontend server:

```bash
npm start
```


## OpenAI API Integration

The exercise suggestion feature uses OpenAI's API. To enable this:

1. Sign up for OpenAI and obtain an API key.
2. Create a .env file in the main directory:
Paste this in the .env
```bash
OPENAI_API_KEY=<YOUR_API_KEY>
```

## Directory Structure
```bash

emo-insight/
├── backend/          # Python Flask backend
│   ├── emotion-server.py
│   ├── requirements.txt
│   └── ...
├── journal/          # React frontend
│   ├── src/
│   ├── package.json
│   └── ...
└── README.md
```


# Usage

### Start the backend server:

```bash
cd backend
source venv/bin/activate  # Activate virtual environment
python emotion-server.py
```

### Start the frontend:

```bash
cd journal
npm start
```

Open the application in your browser at:
```
http://localhost:3000
```


### Acknowledgments
Hugging Face for the pre-trained emotion model.
OpenAI for the exercise suggestion API.
