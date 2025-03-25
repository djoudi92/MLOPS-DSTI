import os
import requests

# Créer le dossier 'data' s'il n'existe pas
os.makedirs("data", exist_ok=True)

# Télécharger le dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
response = requests.get(url)

# Sauvegarder le fichier
with open("data/winequality-red.csv", "wb") as file:
    file.write(response.content)

print("✅ Dataset downloaded successfully in 'data/' folder!")
