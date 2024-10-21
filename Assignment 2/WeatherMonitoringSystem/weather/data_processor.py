
# weather/data_processor.py

from datetime import datetime

class WeatherDataProcessor:
    def process_data(self, data):
        if data:
            city = data['name']
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather_condition = data['weather'][0]['description']
            timestamp = datetime.fromtimestamp(data['dt'])
            return {
                'city': city,
                'temperature': temperature,
                'feels_like': feels_like,
                'weather_condition': weather_condition,
                'timestamp': timestamp
            }
        return None
