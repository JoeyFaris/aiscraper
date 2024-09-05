from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_website
from text_processor import process_text
from tts import text_to_speech

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    raw_text = scrape_website(url)
    processed_text = process_text(raw_text)
    return jsonify({'text': processed_text})

@app.route('/api/tts', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text')
    text_to_speech(text)
    return jsonify({'message': 'Text-to-speech conversion completed successfully.'})

if __name__ == "__main__":
    app.run(debug=True)