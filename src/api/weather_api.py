import requests
import json


def get_weather():
    with open('src/config/weather_configs.json', 'r') as f:
        loaded = json.load(f)
        api_token = loaded['weather_api']
        geolocation = loaded['geolocation']

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_token,
        'q': geolocation,
        'lang': 'pt'
    }

    r = requests.get(url, params=params)
    r = r.json()
    r_dict = r.get("current")

    temperature, weather_condition  = r_dict.get("temp_c"), r_dict.get("condition").get("text")
    weather_img = r_dict.get("condition").get("icon")

    return weather_condition, f"{temperature:.0f}", f'https:{weather_img}'

if __name__ == "__main__":
    print(
        get_weather()
    )