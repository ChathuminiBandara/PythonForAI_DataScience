import requests

# URL for a fake API
url = 'https://jsonplaceholder.typicode.com/posts'

# Parameters to filter the posts
params = {
    'userId': 1,  # Filter posts by user ID
    'id': 1       # Filter for a specific post
}

response = requests.get(url, params=params)

# Print the final URL with query parameters
print("Request URL:", response.url)

# Print the response text
print("Response Text:", response.text)
