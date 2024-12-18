# Steve Stylin@Bellevue University
# Module 12: revise of API's of module 9.2

import requests
import pandas as pd

# API endpoint
url = "https://ssd-api.jpl.nasa.gov/fireball.api?limit=20"

# Test the connection to the API
response = requests.get(url)
# Check Connection Code
if response.status_code == 200:
    print(f"\n{response.status_code}: Connection successful!")
else:
    print(f"Failed to connect: {response.status_code}")

# Print out the response from the request, with no formatting
print(response.text)

# Print out the response with same formatting as the tutorial program
print(response.json())

# Print out the response in a very nice formatted table with header label
data = response.json()['data']
df = pd.DataFrame(data, columns=['year', 'month', 'day', 'time', 'name', 'mass (kg)', 'fall', 'year', 'location'])
print(df)
