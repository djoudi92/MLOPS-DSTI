# Utilise une image Python officielle comme base
FROM python:3.9-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers dans le conteneur
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Lancement de l’application avec Gunicorn
#ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "main:app"]
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:80", "main:app"]