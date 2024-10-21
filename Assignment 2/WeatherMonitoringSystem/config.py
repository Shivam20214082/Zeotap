# config.py

import os

class Config:
    # OpenWeatherMap API Configuration
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY', '95953f0e91c64f0a3c33c17485798124')
    
    # MongoDB Configuration
    MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/weather_db')
