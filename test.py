import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "essen1", "date_added": "10.01.21"},
        {"name": "essen2", "date_added": "10.01.21"},
        {"name": "essen3", "date_added": "10.01.21"}]


for i in range(len(data)):
    response = requests.put(
        BASE + "/food/" + str(i), data[i])
    print(response.json())

response = requests.delete(BASE + "/food/2")
print(response)
response = requests.get(BASE + "/food/1")
print(response.json())
