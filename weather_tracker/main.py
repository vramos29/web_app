#this is the main file

import requests
from dataclasses import dataclass
import app



#Initial URL retrieval of information for 2nd URL
URL1 = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name": app.user_input1, "country": app.user_input2, "count": 1}

response = requests.get(URL1, params=params, timeout = 7)
response.raise_for_status()


#Verifies geo_data to ensure every needed variable/value is in the API response
def check_geo_data():
    geo_data = response.json() 

    if 'results' not in geo_data:
        print("No 'results' found.")
    global results
    results = geo_data['results']

    if 'longitude' not in results or not isinstance(results['longitude'], int):
        return("'Longitude' not found or has incorrect value")
    if 'latitude' not in results or not isinstance(results['latitude'], int):
        return("'Latitude' not found or has incorrect value")
    if 'city' not in results or not isinstance(results['name'], str):
        return("'City' not found or has incorrect value")
    if 'country_code' not in results or not isinstance(results['country_code'], str):
        return("'Country' not found or has incorrect value")

check_geo_data()
longitude = results[0]['longitude'] 
latitude = results[0]['latitude']
city = results[0]['name']
country = results[0]['country_code']



#Takes longitude and latitude parameters and passes them through 2nd URL
URL2 = "https://api.open-meteo.com/v1/forecast?current_weather=true"
params2 = {"latitude": latitude, "longitude": longitude}
response2 = requests.get(URL2, params=params2, timeout = 7)
response2.raise_for_status()


#Verifies meteo_data to ensure every needed variable/value is in the second API response
def check_meteo_data():
    global meteo_data
    meteo_data = response2.json()

    if 'current_weather' not in meteo_data:
        print("No 'results' found.")
    global current_weather
    current_weather = meteo_data['current_weather']

    if 'temp' not in current_weather or not isinstance(current_weather['temperature'], int):
        return("'Temperature' not found or has incorrect value")
    if 'elevation' not in meteo_data or not isinstance(meteo_data['relevation'], int):
        return("'Elevation' not found or has incorrect value")
    if 'windspeed' not in current_weather or not isinstance(current_weather['windspeed'], int):
        return("'City' not found or has incorrect value")
    if 'observation_time' not in current_weather:
        return("'Observation time' not located")

check_meteo_data()
current_weather = meteo_data['current_weather']
temp = current_weather['temperature']
elevation = meteo_data['elevation']
windspeed = current_weather['windspeed']
observation_time = current_weather['time']


#Turns data into python object
@dataclass
class WeatherReport:
    city: str
    country: str
    latitude: float
    longitude: float
    temp: float
    elevation: float
    windspeed: float
    observation_time: str
    
report = WeatherReport(city, country, latitude, longitude, temp, elevation, windspeed, observation_time)

print(report)

        



        


