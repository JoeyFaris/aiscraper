from scraper import scrape_website
from text_processor import process_text
from tts import text_to_speech

def main():
    url = input("Enter the URL to scrape: ")
    raw_text = scrape_website(url)
    processed_text = process_text(raw_text)
    text_to_speech(processed_text)

if __name__ == "__main__":
    main()
