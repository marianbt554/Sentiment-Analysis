from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Hugging Face pipeline for emotion classification
emotion_classifier = pipeline('text-classification', model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json()
        text = data.get('text', '')

        # Basic check to determine if the text is incomprehensible
        if not text.strip() or len(text.split()) < 3:  # Adjust the condition as needed
            return jsonify({'emotions': {'undefined': 1.0}})  # Return 'undefined' for incomprehensible text

        # Emotion analysis using Hugging Face
        emotion_results = emotion_classifier(text)
        emotions = {result['label']: result['score'] for result in emotion_results[0]}

        # If no emotions detected, return 'undefined'
        if not emotions:
            emotions = {'undefined': 1.0}

        # Return detailed emotion analysis
        response = {
            'emotions': emotions
        }

        return jsonify(response)
    
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        return jsonify({'error': 'An error occurred during sentiment analysis'}), 500

if __name__ == '__main__':
    app.run(port=5003)
