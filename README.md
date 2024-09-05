Web Scraper with Text-to-Speech
This project is a web application that allows users to scrape content from a given URL and convert the scraped text to speech. It consists of a React frontend and a Python backend.
Features
Web scraping from user-provided URLs
Text processing of scraped content
Text-to-speech conversion
User-friendly interface
Project Structure
The project is divided into two main parts:
Frontend (fe)
Backend (be)
Frontend
The frontend is built with React and uses Tailwind CSS for styling.
Key files:
;
;
Backend
The backend is built with Python using Flask for the API.
Key files:
)
"
)
Setup
Frontend
Navigate to the fe directory
Install dependencies:
install
Start the development server:
start
Backend
Navigate to the be directory
Create a virtual environment:
venv
Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
4. Install dependencies:
txt
5. Run the Flask application:
py
Usage
Open the web application in your browser (default: http://localhost:3000)
Enter a URL in the input field
Click "Scrape" to fetch and process the content
Click "Read Aloud" to convert the scraped text to speech
Use the "Turn Off" button to stop the speech playback
Technologies Used
Frontend:
React
Axios for API requests
Tailwind CSS for styling
Backend:
Python
Flask for API
BeautifulSoup for web scraping
pyttsx3 for text-to-speech (Windows/Linux)
macOS built-in say command for text-to-speech (macOS)
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is open source and available under the MIT License.
