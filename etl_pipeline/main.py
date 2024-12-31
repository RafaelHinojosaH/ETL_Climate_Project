import os
from dotenv import load_dotenv
from fetch_data import fetch_weather_data
from transform_data import transform_weather_data
from load_data import create_db_engine, load_data_to_db

# Cargar variables del archivo .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
DB_URL = os.getenv("DB_URL")
CITY = "Mexico City"
TABLE_NAME = "weather"

def run_etl():
    """Ejecución principal del pipeline ETL."""
    # 1. Extracción
    raw_data = fetch_weather_data(API_KEY, CITY)

    # 2. Transformación
    transformed_data = transform_weather_data(raw_data)

    # 3. Carga
    engine = create_db_engine(DB_URL)
    load_data_to_db(transformed_data, TABLE_NAME, engine)

if __name__ == "__main__":
    run_etl()
