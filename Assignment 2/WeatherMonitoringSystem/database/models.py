# database/models.py

from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGODB_URI)
db = client.weather_db

def get_user_collection():
    return db.users

def get_weather_data_collection():
    return db.weather_data

