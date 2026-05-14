# WeatherApp

A weather web application built with Django that consumes the OpenWeatherMap API to display real-time weather and 5-day forecasts for any city in the world.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![API](https://img.shields.io/badge/OpenWeatherMap-API-orange)

## Live Demo
🔗 *Coming soon*

## About

WeatherApp is a Django-based web application that lets users search any city and instantly see current weather conditions and a 5-day forecast. Built as a portfolio project to demonstrate backend API consumption, service layer architecture, and clean Django project structure.

## Features

- **City search** — Search any city worldwide by name or ZIP code
- **Current weather** — Temperature, feels like, humidity, wind speed, pressure, visibility
- **Sunrise & Sunset** — Local sunrise and sunset times for the searched city
- **5-Day forecast** — Daily forecast with weather icons, high/low temperatures, and description
- **Tab interface** — Today and 5-Day tabs switch seamlessly without page reload
- **Live navbar** — Navbar updates with the current city, temperature, and icon after every search
- **Error handling** — User-friendly messages for invalid cities, network errors, and server issues
- **Custom error pages** — Styled 404 and 500 pages consistent with the app design

## Tech Stack

- **Backend** — Python, Django
- **External API** — OpenWeatherMap (Current Weather API, 5-Day Forecast API, Geocoding API)
- **Frontend** — Vanilla CSS (glassmorphism, gradients), Vanilla JavaScript (tab switching)
- **Static files** — WhiteNoise
- **Config** — python-decouple for environment variables

## Project Structure

```
WeatherApp/           # Project settings and root URLs
weather/              # Core app — views, services, templates
    services.py       # All OpenWeatherMap API logic located here
    views.py          # Thin views that call services and render templates
templates/            # Project-level base template and error pages
static/               # CSS
```

## Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/Gongzuo-Dk/WeatherApp.git
cd WeatherApp
```

**2. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Get an OpenWeatherMap API key**

Register for free at [openweathermap.org](https://openweathermap.org/api) and grab your API key from the dashboard.

**5. Create a `.env` file in the project root**
```
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
OPENWEATHER_API_KEY=your_api_key_here
```

**6. Apply migrations**
```bash
python manage.py migrate
```

**7. Collect static files**
```bash
python manage.py collectstatic
```

**8. Run the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Key Implementation Details

- **Service layer** — All OpenWeatherMap API communication is isolated in `services.py`, completely separate from views. Views stay thin and readable — they call a service function and pass the result to the template.
- **Geocoding** — City names are first converted to coordinates via the Geocoding API, then coordinates are used for weather calls. This is the modern recommended approach — direct city name lookup is deprecated by OpenWeather.
- **Two API calls per search** — `get_current_weather()` and `get_forecast()` are separate functions. The forecast is only fetched if the current weather call succeeds, avoiding unnecessary API requests.
- **Forecast parsing** — The forecast API returns 40 entries (every 3 hours for 5 days). The service layer filters for the midday reading of each day to produce a clean 5-entry daily summary.
- **Unix timestamp conversion** — Sunrise and sunset values from the API are raw Unix timestamps, converted to proper Python `datetime` objects in `services.py` so Django's `|date` template filter can format them correctly.
- **Three template states** — The template handles three distinct states: empty (no search yet), error (bad city or API failure), and data (successful response).
- **Environment variables** — All secrets and API keys managed via `python-decouple`. No credentials ever touch the codebase.
- **Static files** — Served via WhiteNoise, which works consistently in both development and production regardless of `DEBUG` setting.

## Screenshots

> *Sceenshots*

## Author

Daniel K
GitHub: https://github.com/Gongzuo-Dk
LinkedIn: https://www.linkedin.com/in/danylo-kulynych/