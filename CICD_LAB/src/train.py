import pandas as pd
import numpy as np
import json
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Charger les données prétraitées
df = pd.read_csv("data/processed.csv")

# Séparer les features et la target
X = df.drop(columns=["quality"])  # La colonne "quality" est la cible
y = df["quality"]

# Diviser les données en train et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paramètres (utilisés par DVC)
learning_rate = 0.1
epochs = 1000

# Entraîner le modèle ElasticNet
model = ElasticNet(alpha=learning_rate, l1_ratio=0.5, max_iter=epochs, random_state=42)
model.fit(X_train, y_train)

# Faire des prédictions
y_pred = model.predict(X_test)

# Évaluer le modèle
metrics = {
    "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
    "MAE": mean_absolute_error(y_test, y_pred),
    "R2": r2_score(y_test, y_pred)
}

# Sauvegarder les métriques
with open("metrics.json", "w") as f:
    json.dump(metrics, f)

# Sauvegarder le modèle
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Training completed. Model and metrics saved.")
