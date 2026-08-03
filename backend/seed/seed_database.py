import json

from pymongo import MongoClient

from app.config.settings import (
    DATABASE_NAME,
    MONGO_URI,
)

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

with open(
    "seed/questions.json",
    encoding="utf-8",
) as file:

    questions = json.load(file)

db.questions.delete_many({})

db.questions.insert_many(questions)

print("✅ Questions Seeded!")