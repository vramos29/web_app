#this is the main file

import requests


URL1 = "https://geocoding-api.open-meteo.com/v1/search"
URL2 = "https://api.open-meteo.com/v1/forecast?current_weather=true"

params = {"name": "Chicago", "country": "United States", "count": 1}
response = requests.get(URL1, params=params, timeout = 12)
response.raise_for_status()


data = response.json()
print(data)

latitude = data['latitude']     #not working
longitude = data['longitude']

print(f"{longitude}, {latitude}")






