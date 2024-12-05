
# Steve Stylin@Bellevue University
# Module 9: API's
import requests
# Test the connection to the Open Notify API
api_url = 'http://api.open-notify.org/astros.json'
response = requests.get(api_url)

# Check Connection Code
if response.status_code == 200:
    print(f"\n{response.status_code}: Connection successful!")
else:
    print(f"Failed to connect: {response.status_code}")

# Print the raw response
#print("Raw response:")
#print(response.text)

# Format and print the response
data = response.json()  # Convert the response to JSON
print("\nFormatted response:")
print(f"Number of astronauts in space: {data['number']}")
print("Names of astronauts:")
for astronaut in data['people']:
    print(f"- {astronaut['name']} on the {astronaut['craft']}")
