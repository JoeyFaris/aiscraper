from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_website
from text_processor import process_text
from tts import text_to_speech, stop_speech
from process_pdf import process_pdf

app = Flask(__name__)
CORS(app)

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

@app.route('/api/tts/stop', methods=['POST'])
def stop_tts():
    data = request.json
    stop_speech()
    return jsonify({'message': 'Text-to-speech stopped successfully.'})

@app.route('/api/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    processed_text, error = process_pdf(file)
    if error:
        return jsonify({'error': error}), 400
    return jsonify({'text': processed_text})

if __name__ == "__main__":
    app.run(debug=True) 