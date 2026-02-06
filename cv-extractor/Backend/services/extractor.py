import re
import unicodedata

# Nettoyage du texte 
def clean_text(text: str):
    text = text.lower()
    text = unicodedata.normalize("NFKD", text)   # enlève accents bizarres
    text = re.sub(r"\s+", " ", text)             # supprime espaces multiples
    return text


# Extraction email 
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else ""


# Extraction téléphone
def extract_phone(text):
    match = re.search(r"(?:\+33|0)[1-9](?:[\s\.-]?\d{2}){4}", text)
    return match.group() if match else ""


# Extraction diplôme 
def extract_degree(text):
    patterns = [
        r"licence",
        r"bachelor",
        r"master",
        r"msc",
        r"ing[eé]nieur",
        r"doctorat",
        r"phd"
    ]

    for p in patterns:
        match = re.search(p, text)
        if match:
            return match.group()

    return ""

# Extraction nom
def extract_nomCandidat(text : str):
    match = re.search(r"^([A-Z][a-z]+)\s+([A-Z][a-z]+)", text)
    return match.group() if match else ""

# Extraction prénom
def extract_prenomCandidat(text : str):
    match = re.search(r"^([A-Z][a-z]+)\s+([A-Z][a-z]+)", text)
    return match.group() if match else ""

# Extraction niveau d'anglais
def extract_niveauAnglais(text: str):
    match = re.search(r"(anglais|english).{0,20}?(a1|a2|b1|b2|c1|c2)", text)
    return match.group(2) if match else ""

