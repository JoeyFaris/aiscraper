import requests
from bs4 import BeautifulSoup
import re

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the main content div
    content_div = soup.find('div', {'id': 'mw-content-text'})
    if content_div:
        # Extract all paragraphs from the content div
        paragraphs = content_div.find_all('p')
        
        # Join the text from all paragraphs
        content = ' '.join([p.get_text() for p in paragraphs])
        
        # Remove citations and extra whitespace
        content = re.sub(r'\[\d+\]', '', content)
        content = re.sub(r'\s+', ' ', content).strip()
        
        return content
    else:
        return "Failed to extract content from the webpage."
