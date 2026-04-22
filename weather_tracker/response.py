#this is the main file

import requests
from dataclasses import dataclass


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


#Initial URL retrieval of information for 2nd URL
def geo_request(city, country):
    URL1 = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "country": country, "count": 1}

    response = requests.get(URL1, params=params, timeout = 7)
    response.raise_for_status()
    geo_data = response.json()
    
    #Verifies geo_data to ensure every needed variable/value is in the API response

    if 'results' not in geo_data or not geo_data["results"]:
        return {"error": "Location not found"}

    result = geo_data['results'][0]

    required_response = ["latitude", "longitude", "name", "country_code"]
    for responses in required_response:
        if responses not in result:
            return {"error": f"Missing required field: {responses}"}

    return {
        "latitude": result['latitude'],
        "longitude": result['longitude'],
        "city": result['name'],
        "country": result['country']
    }



#Takes longitude and latitude parameters and passes them through 2nd URL
def meteo_request(latitude, longitude):


    URL2 = "https://api.open-meteo.com/v1/forecast?current_weather=true"
    params2 = {"latitude": latitude, "longitude": longitude, "current_weather": True}

    meteo_response = requests.get(URL2, params=params2, timeout = 7)
    meteo_response.raise_for_status()
    meteo_data = meteo_response.json()


    #Verifies meteo_data to ensure every needed variable/value is in the second API response


    if 'current_weather' not in meteo_data or not meteo_data['current_weather']:
        return {"error": "Data not found"}

    current_weather = meteo_data['current_weather']

    required_weather_response = ["temperature", "windspeed", "time"]
    for responses in required_weather_response:
        if responses not in current_weather:
            return {"error": f"Missing required field: {responses}"}


    return {
        "temp": current_weather['temperature'],
        "elevation": meteo_data['elevation'],
        "windspeed": current_weather['windspeed'],
        "observation_time": current_weather['time']
    }


#Turns data into python object


def report_form(geo, meteo):
    return WeatherReport(
        city=geo["city"],
        country=geo["country"],
        latitude=geo["latitude"],
        longitude=geo["longitude"],
        temp=meteo["temp"],
        elevation=meteo["elevation"],
        windspeed=meteo["windspeed"],
        observation_time=meteo["observation_time"]
    )