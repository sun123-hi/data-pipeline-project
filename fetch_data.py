import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
data = response.json()

# Save data to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data fetched successfully!")