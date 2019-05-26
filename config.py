from flask import Flask
import requests
import json


url = "https://cat-fact.herokuapp.com/facts"

response = requests.get(url)
data = response.text
parsed = json.loads(data)
print(json.dumps(parsed, indent=4))