import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Chargement du modèle
model = joblib.load("models/best_model.pkl")

st.set_page_config(page_title="Détection maladie cardiaque", layout="wide")
st.title("Prédiction du risque de maladie cardiaque")
st.markdown("""
<style>
    .main {
        background-color: #111827;
        color: white;
    }
    .stApp {
        background-color: #111827;
    }
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stDataFrame, .stButton>button, .stSlider label {
        color: white !important;
    }
    .stAlert-success {
        background-color: #14532d !important;
    }
</style>
""", unsafe_allow_html=True)


# Barre latérale : formulaire utilisateur

st.sidebar.header("Informations médicales")
age = st.sidebar.slider("Âge", 18, 100, 50)
sex = st.sidebar.selectbox("Sexe", ["Homme", "Femme"])
cp = st.sidebar.selectbox("Type de douleur thoracique (cp)", [0, 1, 2, 3])
trestbps = st.sidebar.number_input("Pression artérielle au repos (trestbps)", 80, 200, 120)
chol = st.sidebar.number_input("Cholestérol sérique (chol)", 100, 600, 200)
fbs = st.sidebar.selectbox("Glycémie à jeun > 120 mg/dl", [0, 1])
restecg = st.sidebar.selectbox("Électrocardiogramme au repos", [0, 1, 2])
thalach = st.sidebar.slider("Fréquence cardiaque maximale atteinte (thalach)", 70, 210, 150)
exang = st.sidebar.selectbox("Angine induite par l'effort", [0, 1])
oldpeak = st.sidebar.number_input("Dépression ST", 0.0, 6.0, 1.0, step=0.1)
slope = st.sidebar.selectbox("Pente du segment ST", [0, 1, 2])
ca = st.sidebar.selectbox("Nbre de vaisseaux colorés", [0, 1, 2, 3, 4])
thal = st.sidebar.selectbox("Thalassémie", [0, 1, 2, 3])

# Conversion en DataFrame
sex_val = 1 if sex == "Homme" else 0
input_data = pd.DataFrame([[age, sex_val, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]],
                          columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                                   'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

# Moyennes et écarts-types du dataset (issus de X.mean() et X.std())
mean_values = [54.366, 0.683, 1.032, 131.689, 246.264, 0.148, 0.990, 149.607, 0.326, 1.039, 1.399, 0.729, 2.313]
std_values  = [9.109, 0.466, 1.033, 17.599, 51.830, 0.356, 0.994, 22.905, 0.470, 1.162, 0.616, 1.022, 0.612]

# Appliquer la standardisation manuelle
input_data = (input_data - mean_values) / std_values

# Affichage central : visuels + résultat
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
    st.markdown("""
    ### À propos
    Cette application prédit si un patient présente un **risque de maladie cardiaque** 
    en se basant sur plusieurs indicateurs médicaux reconnus. 

    - Modèle de Machine Learning entraîné avec des données médicale.

    - Résultat instantané et indicatif.
    """)

with col2:
    if st.sidebar.button("Prédire le risque"):
        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0][1]

        st.subheader("Résultat de l'analyse")
        if prediction == 1:
            st.error(f"Risque détecté avec une probabilité de {proba:.2%}.")
        else:
            st.success(f"Aucun risque détecté (probabilité de {proba:.2%}).")

        # Graphique circulaire avec thème foncé et taille adaptative
        fig, ax = plt.subplots(figsize=(4, 4), facecolor='#111827')
        ax.pie([proba, 1 - proba], labels=["Risque", "Pas de risque"], autopct="%.1f%%", colors=["#ff4b4b", "#4CAF50"], textprops={'color':"white"})
        ax.set_title("Probabilité estimée", color="white")
        fig.patch.set_facecolor('#111827')
        st.pyplot(fig)
