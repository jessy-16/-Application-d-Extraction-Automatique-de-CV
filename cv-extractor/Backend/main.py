from fastapi import FastAPI, UploadFile, File
from services.pdf_parser import read_pdf
from services.docx_parser import read_docx
from services.extractor import (
    clean_text,
    extract_email,
    extract_phone,
    extract_degree,
    extract_nomCandidat,
    extract_prenomCandidat,
    extract_niveauAnglais
)

#from models.cv_result import CVResult

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API OK"}

#Endpoint principal 
@app.post("/api/v1/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    content = await file.read() 

    # selon extension
    if file.filename.endswith(".pdf"):
        raw_text = read_pdf(content)
    elif file.filename.endswith(".docx"):
        raw_text = read_docx(content)
    else:
        return {"error": "Format non supporté"}

    text = clean_text(raw_text)

    nomCandidat = extract_nomCandidat(text)
    prenomCandidat = extract_prenomCandidat(text)
    email = extract_email(text)
    phone = extract_phone(text)
    degree = extract_degree(text)
    niveauAnglais = extract_niveauAnglais(text)  

    return {

        "last_name" : nomCandidat,
        "first_name" : prenomCandidat,
        "email": email,
        "phone": phone,
        "degree": degree,
        "anglais": niveauAnglais,
    }
