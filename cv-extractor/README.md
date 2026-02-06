## Extraction Automatique de CV

Application web permettant d’extraire automatiquement des informations depuis un CV (PDF ou DOCX).

## Fonctionnalités
- Upload d’un fichier PDF ou DOCX
- Extraction automatique :
  - Nom
  - Prénom
  - Email
  - Téléphone
  - Diplôme
  - Niveau d’anglais (A1 à C2)
- Téléchargement du résultat au format JSON

## Technologies utilisées
- FastAPI (backend)
- Streamlit (frontend)
- pdfplumber
- python-docx
- regex
- Docker

## Installation (sans Docker)
```bash
git clone https://github.com/ton-compte/cv-extractor.git
cd cv-extractor

#Vous pouvez créer un environnement virtuel si vous le souhaitez

python -m venv venv
venv\Scripts\activate # sous Windows

# On installe les dépendances
#Backend
cd backend
pip install -r requirements.txt

#Frontend
cd ../frontend
pip install -r requirements.txt

#Lancement local
#Backend avec FastAPI
cd backend
uvicorn main:app --reload

http://127.0.0.1:8000
http://127.0.0.1:8000/docs

#Frontend avec Streamlit
cd frontend
streamlit run app.py

http://localhost:8501

#Lancement avec Docker
docker-compose up --build

#Exemples d'API
POST /api/v1/upload-cv
#Avec la commande curl
curl -X POST "http://127.0.0.1:8000/api/v1/upload-cv" \
-F "file=@cv.pdf"

#Exemple de réponse au format JSON
{
  "last_name": "Morales",
  "first_name": "Miles",
  "email": "miles.morales@gmail.com",
  "phone": "0612345678",
  "degree": "bachelor",
  "anglais": "c1"
}

#Structure du projet
cv-extractor/ 
    backend/ 
        main.py 
        requirements.txt 
        services/ 
            pdf_parser.py 
            docx_parser.py 
            extractor.py 
    models/ 
        cv_result.py 
frontend/ 
    app.py 
    requirements.txt 
docker/ 
    Dockerfile.backend 
    Dockerfile.frontend 
docker-compose.yml 
README.md

#Projet réalisé par JESSYCA KIOUBIA