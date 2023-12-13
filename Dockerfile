FROM python:3.10-alpine

# Copiez les fichiers nécessaires dans le conteneur
COPY getgrades.py .
# COPY average.txt .
# COPY grades.txt .
COPY requirements.txt .
COPY .env .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter votre programme Python
CMD ["python", "-u", "getgrades.py"]