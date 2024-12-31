import pandas as pd

def transform_weather_data(raw_data):
    """Transforma los datos de la API en un DataFrame limpio."""
    main_data = raw_data["main"]
    weather_data = raw_data["weather"][0]
    transformed = {
        "city": raw_data["name"],
        "temperature": main_data["temp"],
        "humidity": main_data["humidity"],
        "weather": weather_data["description"],
        "timestamp": pd.to_datetime(raw_data["dt"], unit="s")
    }
    return pd.DataFrame([transformed])