import pymongo
import json

# Replace these with your own MongoDB Atlas connection details
MONGO_URI = "mongodb+srv://nava:sachacks23@cluster.mongodb.net/test"
DB_NAME = "nava"
COLLECTION_NAME = "jd"

with open('technology_keywords.json', "w") as f:
    data_to_insert = json.load(f)

# Sample JSON objects (replace these with your own data)
# data_to_insert = [
#     {
#         "name": "John",
#         "age": 30,
#         "city": "New York"
#     },
#     {
#         "name": "Alice",
#         "age": 25,git push

#         "city": "Los Angeles"
#     },
#     {
#         "name": "Bob",
#         "age": 35,
#         "city": "San Francisco"
#     }
# ]

# Connect to MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Insert JSON objects into the collection
for data in data_to_insert:
    collection.insert_one(data)

# Close the MongoDB connection
client.close()
