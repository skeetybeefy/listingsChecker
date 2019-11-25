from pymongo import MongoClient
import getCases


client = MongoClient('localhost', 27017)
db = client.cases

for item in getCases.createItems():
    collection = db[f"{item['name']}"]
    collection.insert_one(item)







