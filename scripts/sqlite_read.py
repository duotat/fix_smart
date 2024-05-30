import sqlite3
import configparser

# Lire le fichier de configuration
config = configparser.ConfigParser()
config.read('../conf/config.properties')

# Obtenir le chemin de la base de données de la section [sqlite]
db_path = config.get('sqlite', 'db_path')

# Connexion à la base de données
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Sélectionner toutes les lignes de la table refproduct
try:
    c.execute("SELECT * FROM refproduct")
    rows = c.fetchall()

    # Afficher les lignes récupérées
    if rows:
        print("Contenu de la table refproduct:")
        for row in rows:
            print(row)
    else:
        print("La table refproduct est vide.")
except sqlite3.Error as e:
    print(f"Erreur lors de la récupération des données : {e}")

# Fermer la connexion à la base de données
conn.close()
