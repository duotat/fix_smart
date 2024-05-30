from fastapi import FastAPI
from typing import List
from scripts.dataset_read import get_distinct_repair_status
from configparser import ConfigParser


app = FastAPI()

# Fonction pour lire le fichier de configuration
def read_config(filename='conf/config.properties', section='server'):
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return config


# Lire les configurations du fichier config.properties
config = read_config()



# Fonction pour exposer API en fonction de la configuration
@app.get("/getRepairStatus", response_model=List[str])
def get_repair_status():
     # Chemin vers le fichier dataset.csv
    file_path = './dataset/OpenRepairData_v0.1_aggregate_202003.csv'

    # Appeler la fonction get_distinct_repair_status pour obtenir les valeurs distinctes
    distinct_values = get_distinct_repair_status(file_path)
    
    return distinct_values

if __name__ == "__main__":
    import uvicorn
    print("Lancement du serveur uvicorn")  
    uvicorn.run(app, host=config['host'], port=int(config['port']))