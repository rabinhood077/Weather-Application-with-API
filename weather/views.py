
# weather/views.py
import requests
from django.shortcuts import render
from .forms import CityForm

def weather_view(request):
    weather_data = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key ='52e3784073a21e7da86f55b0ac81350'  # Replace this with your OpenWeatherMap API key
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
    else:
        form = CityForm()
    return render(request, 'weather/weather.html', {'form': form, 'weather': weather_data})
