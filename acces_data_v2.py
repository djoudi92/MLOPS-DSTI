import pandas as pd
import dvc.api

path = 'data/wine_original.csv'
repo = 'C:/Users/AbdessalemDjoudi/Desktop/MLOPS-DSTI/data_versioning'  
version = 'v2'  # Change la version ici (v1, v2, v3...)

# Obtenir l'URL de la version spécifique du dataset
data_url = dvc.api.get_url(
    path=path,
    repo=repo,
    rev=version  # Spécifier la version
)

# Charger le dataset
data = pd.read_csv(data_url, sep=";",encoding="ISO-8859-1")
print(data.head())  
