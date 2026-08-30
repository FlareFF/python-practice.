import requests

while True:
    city = input("Enter the city: ")
    if city == "exit":
        print("bye")
        break
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    try:
        geo_dict = requests.get(geo_url).json()

        latitude = geo_dict["results"][0]["latitude"]

        longitude = geo_dict["results"][0]["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

        weather_dict = requests.get(weather_url).json()

        current_temp = weather_dict["current_weather"]["temperature"]

        print(f"Current temperature in {city}: {current_temp} °C")
    except (KeyError, IndexError):
        print("City not found, try again")
