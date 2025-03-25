import pandas as pd

# Charger les données brutes
df = pd.read_csv("data/winequality-red.csv", sep=";")

# Appliquer une normalisation (min-max scaling)
df_normalized = (df - df.min()) / (df.max() - df.min())

# Sauvegarder les données prétraitées
df_normalized.to_csv("data/processed.csv", index=False)

print("Preprocessing completed. Processed data saved to data/processed.csv")
