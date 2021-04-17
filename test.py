import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "/cats/Lou", {"date": "10.01.21"})
print(response.json())
