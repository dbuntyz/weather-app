# Weather App

A simple Flask-based web application that provides current weather information and a 7-day forecast for a given city. The app fetches weather data from the [wttr.in](http://wttr.in) API and presents it in a user-friendly interface.

## Features

- Search for the weather by city name.
- Display current weather conditions (temperature, humidity, wind speed).
- Show a 3-day weather forecast.
- Dynamic background images based on weather conditions.
- Responsive design for mobile and desktop views.

## Technologies Used

- **Frontend:** HTML, CSS, Swiper.js
- **Backend:** Python, Flask
- **API:** [wttr.in](http://wttr.in)
- **Version Control:** Git

## Installation

To run the Weather App locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dbuntyz/weather-app.git
   cd weather-app

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
3. **Upgrade pip to the latest version:**
   ```bash
   pip install --upgrade pip
   pip install requests
   pip install flask
4. **Run the application:**
   ```bash
   python app.py
5. **Open your web browser and go to:**
   ```bash
   http://127.0.0.1:5000
