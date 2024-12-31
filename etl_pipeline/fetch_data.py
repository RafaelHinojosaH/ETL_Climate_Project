import requests

def fetch_weather_data(api_key, city):
    """Extrae los datos climáticos de la API OpenWeather."""
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener datos de la API: {response.status_code}")

