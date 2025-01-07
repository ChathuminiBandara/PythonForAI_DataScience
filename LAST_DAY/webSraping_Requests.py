import requests

respose = requests.get('https://api.github.com/events');
print(respose)