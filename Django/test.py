import json
import requests

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=f771230ab7da7dcecc547d9e600585f5")
data = json.loads(r.text)

weather = data['weather'][0]['description']
print(weather)