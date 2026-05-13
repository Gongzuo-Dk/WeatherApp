from django.shortcuts import render
from .services import get_current_weather, get_forecast

def index(request):
    weather_data = None
    forecast_data = None
    error = None
    city = request.GET.get("city", "").strip()

    if city:
        weather_data = get_current_weather(city)

        if weather_data is None:
            error = f"Could not find weather data for '{city}'. Please check the city name."
        else:
            forecast_data = get_forecast(city)

    context = {
        'weather': weather_data,
        'forecast': forecast_data,
        'error': error,
        'city': city,
    }

    return render(request, "weather/index.html", context)


