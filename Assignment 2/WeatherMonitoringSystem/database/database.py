
# database/database.py

from pymongo import MongoClient
from config import Config

# Create a MongoDB client
client = MongoClient(Config.MONGODB_URI)

# Access the database
db = client.weather_db

def init_db():
    # Create collections if they do not exist
    if 'users' not in db.list_collection_names():
        db.create_collection('users')
    
    if 'weather_data' not in db.list_collection_names():
        db.create_collection('weather_data')
