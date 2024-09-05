# Web Scraper with Text-to-Speech

This project is a web application that allows users to scrape content from a given URL and convert the scraped text to speech. It consists of a React frontend and a Python backend.

## Features

- Web scraping from user-provided URLs
- Text processing of scraped content
- Text-to-speech conversion
- User-friendly interface

## Project Structure

The project is divided into two main parts:
- Frontend (fe)
- Backend (be)

### Frontend
The frontend is built with React and uses Tailwind CSS for styling. Key files:
- `src/App.js`
- `src/components/`

### Backend
The backend is built with Python using Flask for the API. Key files:
- `app.py`
- `scraper.py`
- `text_to_speech.py`

## Setup

### Frontend
1. Navigate to the `fe` directory
2. Install dependencies: `npm install`
3. Start the development server: `npm start`

### Backend
1. Navigate to the `be` directory
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the Flask application: `python app.py`

## Usage

1. Open the web application in your browser (default: http://localhost:3000)
2. Enter a URL in the input field
3. Click "Scrape" to fetch and process the content
4. Click "Read Aloud" to convert the scraped text to speech
5. Use the "Turn Off" button to stop the speech playback

## Technologies Used

- Frontend:
  - React
  - Axios for API requests
  - Tailwind CSS for styling
- Backend:
  - Python
  - Flask for API
  - BeautifulSoup for web scraping
  - pyttsx3 for text-to-speech (Windows/Linux)
  - macOS built-in `say` command for text-to-speech (macOS)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
