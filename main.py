#this is the main file

import requests


URL1 = "https://geocoding-api.open-meteo.com/v1/search"
URL2 = "https://api.open-meteo.com/v1/forecast?current_weather=true"

params = {"name": "Chicago", "country": "United States", "count": 1}
response = requests.get(URL1, params=params, timeout = 7)
response.raise_for_status()
 
data = response.json() 

results = data['results']

longitude = results[0]['longitude']
latitude = results[0]['latitude']

print(f"{latitude}, {longitude}")

# structure -> list containing a dictionary 
#1) get into results, #2 get into list to itrate through it







