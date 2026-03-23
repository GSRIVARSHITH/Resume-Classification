import pdfplumber
from docx import Document

def extract_text_from_pdf(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(filepath):
    doc = Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(filepath):
    if filepath.endswith(".pdf"):
        return extract_text_from_pdf(filepath)
    elif filepath.endswith(".docx"):
        return extract_text_from_docx(filepath)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")