from PyPDF2 import PdfReader
import io
from text_processor import process_text

def process_pdf(file):
    if file and file.filename.lower().endswith('.pdf'):
        pdf_content = file.read()
        pdf_reader = PdfReader(io.BytesIO(pdf_content))
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            # Remove unnecessary information like page numbers, headers, etc.
            cleaned_text = ' '.join(line.strip() for line in page_text.split('\n') if line.strip())
            text += cleaned_text + ' '
        processed_text = process_text(text)
        # Remove any remaining unnecessary spaces or newlines
        processed_text = ' '.join(processed_text.split())
        return processed_text, None
    else:
        return None, 'Invalid file format. Please upload a PDF.'
