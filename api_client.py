import urllib.request
import json

city = input("Enter the city: ")
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = urllib.request.urlopen(geo_url)

data_geo_url = geo_response.read()

geo_dict = json.loads(data_geo_url)

latitude = geo_dict["results"][0]["latitude"]
longitude = geo_dict["results"][0]["longitude"]

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = urllib.request.urlopen(url)

data = response.read()
weather_dict = json.loads(data)

current_temp = weather_dict["current_weather"]["temperature"]
print(f"Current temperature: {current_temp} °C")
