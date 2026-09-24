"""
Name: Drew Byford
Assignment: Module 9 - APIs
Purpose: Connect to an API, test the connection,
display the raw response, and display formatted JSON.
"""

import requests
import json


# API URL
url = "https://jsonplaceholder.typicode.com/posts/1"


# Send request to API
response = requests.get(url)


# Test the connection
print("API Connection Test")
print("-------------------")
print("Status Code:", response.status_code)


# Print raw response
print("\nUnformatted Response")
print("--------------------")
print(response.text)


# Convert response to JSON
data = response.json()


# Print formatted response
print("\nFormatted Response")
print("------------------")
print(json.dumps(data, indent=4))