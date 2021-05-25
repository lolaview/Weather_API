import urllib.request
import json
from django.shortcuts import render
#from .forms import WeatherForm


def index(request):
    ##getbut = request.POST.get("submit")
    ######location = form.cleaned_data.get('city')

    if request.method == 'POST':
        try:
            city = request.POST['city']
        except KeyError:
            city = 'Oyo'
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                 city + '&units=metric&appid=be0c0b6beaf98b1c1646c6083a8e9cb7').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": (list_of_data["sys"]["country"]),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
            'city':str(city),
        }
        print(data)
    else:
        data = {}

    return render(request, "weather.html", data)