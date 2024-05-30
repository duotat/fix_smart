import pandas as pd

'''Methode to read in csv and return values filtered'''
def get_distinct_repair_status(file_path) :
   
    # Lire le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(file_path)

    # Afficher les valeurs distinctes de la colonne repair_status
    distinct_values = df['repair_status'].unique()
    print("Valeurs distinctes de la colonne 'repair_status' :")
    print(distinct_values)
    return distinct_values