import pandas as pd
import dvc.api

path = 'data/wine_original.csv'
repo = 'C:/Users/AbdessalemDjoudi/Desktop/MLOPS-DSTI/data_versioning'  

data_url = dvc.api.get_url(
    path=path,
    repo=repo
)

# Essaye avec ISO-8859-1 (ou latin1 si ça ne fonctionne pas)
data = pd.read_csv(data_url, sep=";", encoding="ISO-8859-1")
print(data.head())
