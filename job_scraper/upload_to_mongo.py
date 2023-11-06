import pymongo
import json

# Replace these with your own MongoDB Atlas connection details
MONGO_URI = ""
DB_NAME = "nava"
COLLECTION_NAME = "jd"

with open('technology_keywords.json', "r") as f:
    data_to_insert = json.load(f)
    
    

# Connect to MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Insert JSON objects into the collection
for data in data_to_insert:
    collection.insert_one(data)

# Close the MongoDB connection
client.close()
