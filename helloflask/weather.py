import json
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv("OPENWEATHER_API_KEY")


def get_temp(city):
    """"""
    city = city.replace(" ", "%20")
    country_code = "us"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}&units=imperial"

    print(url)  # Open this URL in your browser to see the data

    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode("utf-8")
        weather_data = json.loads(response_text)

    # print(weather_data)
    return weather_data["main"]["temp"]


if __name__ == "__main__":
    print(get_temp("Wellesley"))
    print(get_temp("Miami"))
    print(get_temp("New York"))
