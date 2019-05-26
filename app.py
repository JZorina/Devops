from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


url = "https://cat-fact.herokuapp.com/facts"

response = requests.get(url)
data = response.text
parsed = json.loads(data)
print(json.dumps(parsed, indent=4))



if __name__ == '__main__':
    app.run()
