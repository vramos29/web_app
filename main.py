#this is the main file

import requests

URL1 = "https://geocoding-api.open-meteo.com/v1/search"
URL2 = "https://api.open-meteo.com/v1/forecast?current_weather=true"

params = {"name": "Chicago", "country": "United States", "count": 1}
response = requests.get(URL1, params=params, timeout = 12)
print("Status:", response.status_code)                                    
print("Reponse:",response.json()) 

