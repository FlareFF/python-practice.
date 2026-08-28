import urllib.request
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=47.37&longitude=8.54&current_weather=true"

response = urllib.request.urlopen(url)

data = response.read()
weather_dict = json.loads(data)

current_temp = weather_dict["current_weather"]["temperature"]
print(f"Current temperature: {current_temp} °C")
