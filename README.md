# MLOps Project: Wine Quality Prediction

## 📊 Objectif principal

Ce projet a pour but de mettre en œuvre les bonnes pratiques de MLOps pour un projet de prédiction de la qualité du vin à partir de caractéristiques physico-chimiques.

On y apprend à :

- Gérer les versions des données, du code et des modèles
- Tester la qualité des données
- Suivre les expériences avec MLflow
- Automatiser le pipeline avec GitHub Actions et DVC

---

## 🗃️ 1. Versioning de données avec DVC

- Initialisation de DVC : `dvc init`
- Suivi du fichier `wine_original.csv` : `dvc add`
- Sauvegarde des métadonnées avec Git
- Création d'un stockage distant local : `dvc remote add -d myremote <chemin>`
- Push des données : `dvc push`
- Tag des versions de dataset : `git tag -a "v1" -m "raw data v1"`, etc.

**Objectif :** assurer la traçabilité des données.

---

## 🔬 2. Testing des données et du code

- Installation : `pytest`, `ydata-profiling`, `ipytest`, `great_expectations`
- Génération d'un rapport de profiling : `ProfileReport(data)`
- Écriture de tests de données : types, valeurs manquantes, etc.
- Utilisation de `pytest` pour tester les fonctions

**Objectif :** garantir la qualité des données et du code avant l'entraînement.

---

## 🧪 3. Suivi d'expériences avec MLflow

- Entraînement de modèles `ElasticNet` et `RandomForest`
- Suivi des expériences avec `mlflow.log_param`, `log_metric`, `log_model`
- Lancement de l'interface : `mlflow ui` ([http://localhost:5000](http://localhost:5000))
- Ajout de `input_example` pour les warnings

**Objectif :** comparer facilement les modèles et leurs performances.

---

## 🚀 4. Automatisation avec GitHub Actions et CML

- Nouveau repo `CICD_DSTI`
- Workflow YAML dans `.github/workflows/model_evaluation.yaml`
- À chaque push :
  - Installation des dépendances
  - Exécution du script d'entraînement
  - Création d'un `report.md`
  - Envoi d'un commentaire dans le PR

**Objectif :** automatiser les tests de performance du modèle.

---

## 📆 5. Pipelines avec DVC

- Fichier `dvc.yaml` définit les étapes : `preprocess` → `train`
- Utilisation de `dvc repro` pour relancer automatiquement si les fichiers changent

**Objectif :** automatiser et organiser le pipeline de bout en bout.

---

## 🌐 6. Partage et collaboration

- Utilisation de `ngrok` pour partager le dashboard MLflow en ligne : `ngrok http 5000`

**Objectif :** permettre à d'autres de visualiser et comparer les résultats.

---

## 📃 Répertoires importants

```
MLOPS-DSTI/
├── data_versioning/              # Lab DVC
├── tests/                        # Tests unitaires (pytest)
├── notebooks/                    # Jupyter Notebooks
├── mlruns/                       # Tracking MLflow
├── src/                          # Scripts Python (train, preprocess, etc.)
├── .github/workflows/            # CI/CD config YAML
└── requirements.txt              # Dépendances
```

---

## 🔧 Technologies principales

- **DVC** : gestion de version des données
- **MLflow** : suivi des expériences
- **GitHub Actions + CML** : automatisation
- **pytest / ydata-profiling** : test de données

---

## 📅 Auteur

**Djoudi Abdessalem**



pip install -r requirements.txt
pip freeze > requirements.txt
