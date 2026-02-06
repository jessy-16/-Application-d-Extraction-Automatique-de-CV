import streamlit as st
import requests
import json

st.title("Extraction Automatique de CV")
# On charge le fichier
cv_upload = st.file_uploader("Choisissez un fichier", type = ["pdf", "docx"])

if cv_upload is not None : 
    st.success("Fichier chargé avec succès")

    response = requests.post("http://127.0.0.1:8000/api/v1/upload-cv", files = {"file": (cv_upload.name, cv_upload.getvalue(), cv_upload.type)}
)  

    if response.status_code == 200 : 
        data = response.json()

        st.download_button(
    label="Télécharger le résultat en JSON",
    data = json.dumps(data, ensure_ascii=False, indent=2),
    file_name="resultat_cv.json",
    mime="application/json"
)
        st.subheader("Résultat extrait :")
        st.json(data)
    else:
        st.error("Erreur lors de l'envoi du fichier")

     
