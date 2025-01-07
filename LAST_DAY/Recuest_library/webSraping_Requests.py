import requests

response = requests.get('https://api.github.com/events');
print(response)
print(response.status_code)

if response.status_code == 200:
    if 'application/json' in response.headers.get(('Content-Type')):
        data = response.json()
        print(data)
elif response.status_code == 400:
    print("Response SUCCESS : " ,response);
    print("Header SUCCESS :" ,response.headers);
    content_type = response.headers['Content-Type']
    print("Content Type of the header : " ,content_type)
    print("Response : " , response)
    print(response.text)

elif response.status_code == 404:
    print("Response NOT FOUND: " , response)  
elif response.status_code == 500:
    print("Response INTERNEL SERVER ERROR : " , response)  
else:
    print("Not 200")