# Weather API Key

import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
city = "Eldoret"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


response = requests.get(url)
response.raise_for_status()
data = response.json()

print("Status code:", response.status_code)
print()
print("Data received:", data)
print("-"*140)

print("Current Weather in", city, "-", data["sys"]["country"] + ":")
print("Temperature:", data["main"]["temp"], "°C")
print("Weather conditions:", data["weather"][0]["description"])
print("Humidity:", data["main"]["humidity"], "%")
print("Wind Speed:", data["wind"]["speed"], "m/s")
print("="*140)

