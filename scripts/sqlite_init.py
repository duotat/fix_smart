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

# Création de la table refproduct
c.execute("""
CREATE TABLE IF NOT EXISTS refproduct (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

#enregistrement les changements 
conn.commit()

#fermer la connexion
conn.close()