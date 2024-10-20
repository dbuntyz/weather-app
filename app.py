from flask import Flask, render_template, request  # Import required Flask classes
import requests  # Import requests for making API calls

app = Flask(__name__)

# Home page to accept city input
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch weather data based on city name
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    
    if city:
        # Fetch weather data in JSON format
        url = f"http://wttr.in/{city}?format=j1"  # JSON format
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
            
            # Debugging: Print the weather data
            print(weather_data)

            # Check if the response contains current weather conditions
            if 'current_condition' in weather_data and weather_data['current_condition']:
                # Extract current weather information
                current_condition = weather_data['current_condition'][0]['weatherDesc'][0]['value'].lower()
                temp = weather_data['current_condition'][0]['temp_C']
                humidity = weather_data['current_condition'][0]['humidity']
                wind = weather_data['current_condition'][0]['windspeedKmph']

                # Define a dictionary to map weather conditions to image URLs
                weather_images = {
                    'sunny': 'https://img.freepik.com/free-vector/sunny-weather-background-vector-brown-with-cute-doodle-illustrations_53876-105740.jpg',
                    'partly cloudy': 'https://img.freepik.com/free-vector/airy-fluffy-cloudy-sky-wallpaper-with-text-space_1017-54409.jpg',
                    'cloudy': 'https://img.freepik.com/free-vector/sunny-weather-background-vector-brown-with-cute-doodle-illustrations_53876-105740.jpg',
                    'rain': 'https://img.freepik.com/free-vector/rainy-weather-background-vector-illustration_53876-87959.jpg',
                    'snow': 'https://img.freepik.com/free-vector/snowy-background_53876-96458.jpg',
                    'storm': 'https://img.freepik.com/free-vector/stormy-weather-background_53876-96241.jpg',
                    'mist': 'https://img.freepik.com/free-vector/misty-background_53876-124324.jpg',
                    'fog': 'https://img.freepik.com/free-vector/foggy-background_53876-124325.jpg'
                }

                # Extract 3-day forecast
                forecast = []
                for day in weather_data['weather'][:3]:  # Fetch only the first 3 days
                    condition = day['hourly'][4]['weatherDesc'][0]['value'].lower()
                    day_data = {
                        'date': day['date'],
                        'avgtemp': day['avgtempC'],
                        'mintemp': day['mintempC'],
                        'maxtemp': day['maxtempC'],
                        'condition': condition,
                        'background_url': weather_images.get(condition, 'https://example.com/default.jpg')  # Default image if not found
                    }
                    forecast.append(day_data)

                # Simple icon logic for current weather
                icon = "🌍"  # Default icon if none match
                if "sunny" in current_condition:
                    icon = "☀️"
                elif "cloud" in current_condition:
                    icon = "☁️"
                elif "rain" in current_condition:
                    icon = "🌧️"
                elif "snow" in current_condition:
                    icon = "❄️"
                elif "storm" in current_condition:
                    icon = "🌩️"
                elif "fog" in current_condition:
                    icon = "🌫️"

                # Render result page with current weather and 3-day forecast
                return render_template('result.html', 
                                       city=city, 
                                       temp=temp, 
                                       humidity=humidity, 
                                       wind=wind, 
                                       icon=icon, 
                                       forecast=forecast)
            else:
                # If the weather data is not valid, show location not found message
                return render_template('result.html', city=city, weather="Error: Location not found.", icon="🌍")
        else:
            # If the status code is not 200, return a specific error message
            return render_template('result.html', city=city, weather="Error: Location not found.", icon="🌍")
    else:
        # Handle the case where no city was provided
        return render_template('result.html', city=city, weather="Error: No city provided.", icon="🌍")

if __name__ == '__main__':
    app.run(debug=True)
