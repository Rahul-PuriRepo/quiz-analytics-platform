from pymongo import MongoClient
from pymongo.database import Database

from app.config.settings import (
    MONGO_URI,
    DATABASE_NAME,
)

client = MongoClient(MONGO_URI)

# Force a connection attempt
client.admin.command("ping")

print("✅ Connected to MongoDB Atlas")

db: Database = client[DATABASE_NAME]