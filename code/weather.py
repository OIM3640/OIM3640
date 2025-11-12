# Build a terminal based weather checker
# It should ask user to enter a city, and show the current temperature

import json
import os
import urllib.request


from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv("OPENWEATHER_API_KEY")


def find_temp(city):
    """Return the curren temp for a given city, everythin that involves API"""
    city = city.replace(" ", "%20")
    country_code = "us"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}&units=imperial"

    # print(url)

    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode("utf-8")
        weather_data = json.loads(response_text)
        return weather_data["main"]["temp"]


def app():
    """Create the dialog in terminal to ask user for city name, and display the curren temp"""
    city = input("Please enter a city name (in US): ")
    temp = find_temp(city)
    print(f"The current temperature in {city} is {temp} degree.")


def main():
    """"""
    # print(find_temp("Wellesley"))
    app()


if __name__ == "__main__":
    main()
