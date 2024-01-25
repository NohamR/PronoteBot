# PronoteBot

PronoteBot est un projet conçu pour faciliter la récupération des notes Pronote et envoyer des mises à jour à un webhook. Il utilise la bibliothèque [pronotepy](https://github.com/bain3/pronotepy) pour les interactions avec Pronote.

## Dépendances

 - [pronotepy](https://github.com/bain3/pronotepy)
 - python-dotenv (optionnel)
 - requests

## Utilisation

Pour utiliser PronoteBot, suivez ces étapes :

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/NohamR/PronoteBot.git
   cd PronoteBot
    ```

2. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```


3. Configurez vos variables d'environnement en créant un fichier .env avec le contenu suivant :
    
    ```bash
    DISCORD_WEBHOOKS_PRONOTE=your_discord_webhook_url
    ENT_USERNAME=your_ent_username
    ENT_PASSWORD=your_ent_password
    ENT=name_of_ent 
    ```

Pour avoir le nom de votre ent : [ici](https://pronotepy.readthedocs.io/en/stable/api/ent.html), par exemple : ile_de_france.

4. Exécutez le script PronoteBot :
    
    ```bash
    python3 getgrades.py
    ```


## Docker

Vous pouvez également construire et exécuter PronoteBot en tant que conteneur Docker. Utilisez les configurations Dockerfile et docker-compose.yaml suivantes :

### Dockerfile

Le fichier Dockerfile est disponible [ici](Dockerfile). Assurez-vous de le placer à la racine du répertoire PronoteBot.

Pour construire l'image Docker, exécutez la commande suivante à la racine du répertoire PronoteBot :

    docker build -t PronoteBot:latest .
    docker run -d PronoteBot:latest

### docker-compose.yaml

Le fichier docker-compose.yaml  est disponible [ici](docker-compose.yaml). Assurez-vous de le placer à la racine du répertoire PronoteBot.

    docker-compose up -d
