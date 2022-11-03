from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.environ.get('DATABASE_URL')

# Connect to MongoDB
client = MongoClient(database_url)
# Define the database we are using.
db = client.get_database('flask-app')
# Define the collection we are using.
db_energy_consumption = db.get_collection('EnergyConsumption')
