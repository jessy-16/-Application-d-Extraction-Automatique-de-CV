from docx import Document
from io import BytesIO

# Lecture DOCX 
def read_docx(file_bytes: bytes):
    doc = Document(BytesIO(file_bytes))
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + " "
    return text