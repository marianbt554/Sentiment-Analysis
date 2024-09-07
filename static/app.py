from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    sentiment_scores = sia.polarity_scores(text)
    sentiment = 'neutral'
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'happy'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'sad'
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(port=5003)
