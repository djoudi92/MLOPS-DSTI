from flask import Flask, request, jsonify
import pickle
from model_files.ml_model import predict_wine_quality

# Création de l'app Flask
app = Flask("wine_app")

@app.route("/test", methods=["GET"])
def test():
    return "📣 L'API fonctionne correctement !"

@app.route("/predict", methods=["POST"])
def predict():
    # Récupération des données JSON
    wine_sample = request.get_json()
    print(" Données reçues :", wine_sample)

    # Chargement du modèle
    with open("./model_files/model.bin", "rb") as f_in:
        model = pickle.load(f_in)

    # Prédiction
    predictions = predict_wine_quality(wine_sample, model)
    formatted_result = [int(el) for el in predictions]  # Éviter erreur JSON (int64)
    return jsonify(formatted_result)

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=9696)
    port = int(os.environ.get("PORT", 80))
    app.run(debug=False, host="0.0.0.0", port=port)
