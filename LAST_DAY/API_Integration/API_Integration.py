import requests

url = 'https://api.open-meteo.com/v1/forecast'

params = {
    'latitude': 51.5074,            
    'longitude': -0.1278,
    'current_weather': True        
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Request was successful!")
    weather_info = response.json()
    print(weather_info)
else:
    print(f"Failed to fetch the data. Status code: {response.status_code}")
