import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_WORDS = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)          # collapse whitespace
    text = re.sub(r'[^\x00-\x7F]+', ' ', text) # remove non-ASCII
    return text.strip()

def tokenize(text):
    tokens = word_tokenize(text.lower())
    return [t for t in tokens if t.isalpha() and t not in STOP_WORDS]

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'(\+?\d[\d\s\-]{8,15})', text)
    return match.group(0).strip() if match else None

def extract_name(text):
    lines = text.strip().split('\n')
    for line in lines[:5]:
        line = line.strip()
        if 2 <= len(line.split()) <= 4 and line.replace(' ', '').isalpha():
            return line
    return "Not found"