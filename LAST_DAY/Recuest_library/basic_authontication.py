import requests

url = 'httpss://httpbin.org/get'

username = 'user'
password = 'pass'

response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    print('Authontication Successfull !')
    print(response.text)
else:
    print(f'Authontication Failed . Statys code: {response.status_code}')