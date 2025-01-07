import requests


data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://httpbin.org/post', data);


if response.status_code == 200:
    print('Login Success !')
    print(response.text)
elif response.status_code == 400:
    print()
elif response.status_code == 404:
    print("Response NOT FOUND: " , response)  
elif response.status_code == 500:
    print("Response INTERNEL SERVER ERROR : " , response)  
else:
    print("Not 200")