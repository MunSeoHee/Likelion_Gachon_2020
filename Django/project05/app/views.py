from django.shortcuts import render
import json
import requests
# Create your views here.
def index(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        print(city)
    else:
        city = 'Seoul'
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f771230ab7da7dcecc547d9e600585f5")
    data = json.loads(r.text)
    weather = data['weather'][0]['description']
    temp1 = data['main']['temp_min'] - 273.15
    temp2 = data['main']['temp_max'] - 273.15
    return render(request, 'index.html', {'w':weather, 't1':temp1, 't2':temp2})