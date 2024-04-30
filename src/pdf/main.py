import PyPDF2
import re
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
    return text

def find_dois(text):
    # DOI regex pattern
    doi_pattern = r'\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b'
    return re.findall(doi_pattern, text, re.IGNORECASE)

def extract_dois_from_folder(folder_path):
    dois = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)
            dois.extend(find_dois(text))
    return set(dois)  # Remove duplicates

# Example usage
folder_path = '/Users/isabellechen/Desktop/CRISPR\ Research\ Paper/Mike_s\ Papers'
extracted_dois = extract_dois_from_folder(folder_path)
print(extracted_dois)
