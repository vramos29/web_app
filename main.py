#this is the main file

import requests

#Initial URL retrieval of information for 2nd URL
URL1 = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name": "Chicago", "country": "United States", "count": 1}
response = requests.get(URL1, params=params, timeout = 7)
response.raise_for_status()
 
geo_data = response.json() 

results = geo_data['results']           
longitude = results[0]['longitude'] 
latitude = results[0]['latitude']
city = results[0]['name']
country = results[0]['country_code']




#Takes longitude and latitude parameters and passes them through 2nd URL
URL2 = "https://api.open-meteo.com/v1/forecast?current_weather=true"
params2 = {"latitude": latitude, "longitude": longitude}
response2 = requests.get(URL2, params=params2, timeout = 7)
response2.raise_for_status()

meteo_data = response2.json()

print(meteo_data)

current_weather = meteo_data['current_weather']
temperature = current_weather['temperature']
elevation = meteo_data['elevation']
windspeed = current_weather['windspeed']
observation_time = current_weather['time']



#Turns data into python object

report = {}

class Weather_Info:
    def __init__(self, city, country, latitude, longitude, temperature, elevation, windspeed, observation_time):
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature
        self.elevation = elevation
        self.windspeed = windspeed
        self.observation_time = observation_time
    
    def form_report(self):
        global report
        report = {
            "City": self.city,
            "Country": self.country,
            "Latitude": f"{self.latitude}°",
            "Longitude": f"{self.longitude}°",
            "Temperature": f"{self.temperature}°C",
            "Elevation": self.elevation,
            "Windspeed": f"{self.windspeed} km/h",
            "Obersation Time": self.observation_time
            }
        return report
    

        


