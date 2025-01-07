import requests
import json

def pass_weather_data(new_item):
    current_weather = new_item.get('current_weather')
    temperature = current_weather.get('temperature')
    wind_speed = current_weather.get('windspeed')
    return temperature, wind_speed

def fetch_weather(latitude, longitude):
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': True
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        new_item = response.json()
        return new_item 
    else:
        return None  

weather_data = fetch_weather(51.5074, -0.1278)  

if weather_data:
    temperature, wind_speed = pass_weather_data(weather_data)
    print(f"Temperature: {temperature}")
    print(f"Wind Speed: {wind_speed} ")
