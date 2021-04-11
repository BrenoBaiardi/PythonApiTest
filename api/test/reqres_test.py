import requests
import json

response = requests.get("https://reqres.in/api/users")

for item in response.json()["data"]:
    print(item["email"])