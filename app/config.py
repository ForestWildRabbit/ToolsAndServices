import os

from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGODB_URL)
db = client['mydatabase']
items_collection = db['items']
user_collection = db["users"]

START_USERS_NUMBER = 1000
