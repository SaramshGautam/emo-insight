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
git clone <repository-url>
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

6. Run the backend server:

```bash
python emotion-server.py
```
