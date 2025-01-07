import requests
from bs4 import BeautifulSoup

url = 'http://example.com'
response = requests.get(url)

if response.status_code == 200:
    print("Request was successful!")
    soup = BeautifulSoup(response.content, 'html.parser')
    main_heading = soup.find('h1')
    
    if main_heading:
        print("Main Heading Text:", main_heading.text)
    else:
        print("No <h1> tag found on the webpage.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
