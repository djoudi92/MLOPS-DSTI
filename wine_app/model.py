import warnings
import logging
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn

from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle  # Pour sauvegarder le modèle en .bin

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def train_and_save_model(alpha=1.0, l1_ratio=0.9, model_output_path="model_files/model.bin"):
    logging.basicConfig(level=logging.WARN)
    logger = logging.getLogger(__name__)

    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Charger les données
    csv_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
    try:
        data = pd.read_csv(csv_url, sep=';')
    except Exception as e:
        logger.exception("Unable to download training & test CSV: %s", e)
        return

    # Split data
    train, test = train_test_split(data, test_size=0.25)
    train_x = train.drop("quality", axis=1)
    test_x = test.drop("quality", axis=1)
    train_y = train["quality"]
    test_y = test["quality"]

    # Entraînement
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    model.fit(train_x, train_y)

    # Évaluation
    predicted = model.predict(test_x)
    rmse, mae, r2 = eval_metrics(test_y, predicted)

    print(f"ElasticNet(alpha={alpha}, l1_ratio={l1_ratio})")
    print(f"RMSE: {rmse:.3f}")
    print(f"MAE: {mae:.3f}")
    print(f"R2: {r2:.3f}")

    # Enregistrement des métriques
    with open("metrics.txt", "w") as f:
        f.write(f"RMSE: {rmse}\nMAE: {mae}\nR2: {r2}")

    # Logging avec MLflow
    mlflow.set_experiment("wine_app_experiment")
    
    with mlflow.start_run(run_name = f"ElasticNet (alpha={alpha}, l1_ratio={l1_ratio})"):
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)
        input_example = train_x.iloc[[0]]
        mlflow.sklearn.log_model(model, "model", input_example=input_example)
        print("Modèle et métriques enregistrés avec MLflow.")

    # Sauvegarde avec pickle
    with open(model_output_path, 'wb') as f_out:
        pickle.dump(model, f_out)
        print(f"Modèle sauvegardé dans {model_output_path}")

if __name__ == "__main__":
    train_and_save_model()
