"""
Name: Drew Byford
Assignment: Module 9 - APIs
Purpose: Connect to the Open Notify API and display
information about astronauts currently in space.
"""

import requests
import json


# Send a GET request to the Open Notify astronaut API.
response = requests.get("http://api.open-notify.org/astros.json")


# Display the HTTP status code.
print("Status Code:")
print(response.status_code)


# Display the raw JSON response.
print("\nRaw Response:")
print(response.json())


# Function used to format JSON output.
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# Display the formatted JSON response.
print("\nFormatted Astronaut Data:")
jprint(response.json())