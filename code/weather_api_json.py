data = {
    "coord": {"lon": -71.2926, "lat": 42.2965},
    "weather": [
        {"id": 701, "main": "Mist", "description": "mist", "icon": "50d"},
    ],
    "base": "stations",
    "main": {
        "temp": 47.62,
        "feels_like": 43.38,
        "temp_min": 45.99,
        "temp_max": 49.68,
        "pressure": 1020,
        "humidity": 84,
        "sea_level": 1020,
        "grnd_level": 1014,
    },
    "visibility": 3219,
    "wind": {"speed": 9.22, "deg": 20},
    "clouds": {"all": 100},
    "dt": 1761768783,
    "sys": {
        "type": 2,
        "id": 2093979,
        "country": "US",
        "sunrise": 1761736488,
        "sunset": 1761774165,
    },
    "timezone": -14400,
    "id": 4954738,
    "name": "Wellesley",
    "cod": 200,
}


# print(data['main']['temp'])
print(data["weather"][0]["description"])
