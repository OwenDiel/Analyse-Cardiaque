# 📘 Génération du README.md et requirements.txt pour le projet

readme_content = """# 💓 Prédiction de Maladie Cardiaque

Ce projet utilise un modèle de Machine Learning pour prédire si un patient présente un **risque de maladie cardiaque**, à partir de caractéristiques cliniques simples. L'application est déployée via **Streamlit**.

---

## 📁 Structure du projet

```
├── app.py                       # Code de l'application
├── models/
│   └── best_model.pkl           # Modèle entraîné et sauvegardé avec joblib
├── data/
│   └── heart_disease_clean.csv     # Données nettoyées
│   └── HeartDiseaseUCI.csv          #Données d'origine
├── notebooks/
│   ├── data_exploration.ipynb
│   └── model_training.ipynb
├── README.md
└── requirements.txt
└── .gitignoore

```

---

##  Lancer l'application

### 1. Cloner le projet et installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Lancer l'application Streamlit

```bash
streamlit run app/streamlit_app.py
```

L'interface s'ouvre automatiquement dans le navigateur 🌐

---
## Aperçu de l'application

![Interface Streamlit](![alt text](image-1.png))

##  Fonctionnalités

- Formulaire intuitif dans la barre latérale
- Image et design personnalisés pour le thème médical
- Prédiction de la probabilité de risque
- Affichage dynamique du résultat sous forme de graphique circulaire
- Aucune base de données nécessaire : prédiction en local

---

##  Variables utilisées

- `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`
- `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`

Ces variables sont normalisées dans le modèle entraîné.

---

##  Modèle

Le modèle utilisé est un classificateur de Machine Learning entraîné à partir de données publiques sur les maladies cardiaques. Il a été sauvegardé via `joblib`.

---

##  Remerciements

Projet développé dans un contexte de santé numérique et apprentissage automatique, à des fins pédagogiques et de sensibilisation.

---

##  Contact

- **Nom** : Owen Mouketou  
- **Email** : [mouketoudielowen@gmail.com](mailto:mouketoudielowen@gmail.com)  
- **LinkedIn** : [linkedin.com/in/owen-mouketou](https://linkedin.com/in/owen-mouketou)
"""

requirements_txt = """streamlit
pandas
numpy
matplotlib
scikit-learn
joblib
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

with open("requirements.txt", "w") as f:
    f.write(requirements_txt)

print("README.md et requirements.txt générés avec succès.")
