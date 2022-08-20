from bs4 import BeautifulSoup
import requests
import pymongo
import re

conn = pymongo.MongoClient()
actor_db = conn.cine21
text_collection = actor_db.text_collection

# text_collection.insert_many(
#     [
#         { "name": "Java Hut", "description": "Coffee and cakes", "ranking": 1 },
#         { "name": "Burger Buns", "description": "Java hamburgers", "ranking": 2 },
#         { "name": "Coffee Shop", "description": "Just coffee", "ranking": 3 },
#         { "name": "Clothes Clothes Clothes", "description": "Discount clothing", "ranking": 4 },
#         { "name": "Java Shopping", "description": "Indonesian goods", "ranking": 5 }
#     ]
# )

result = text_collection.find({'name' : {'$regex': 'Co.*'}})
for r in result:
    print(r)

text_collection.create_index([('name', pymongo.TEXT)])

print(text_collection.index_information())
docs = text_collection.find({'$text': {'$search': 'coffee'}})
for doc in docs:
    print(doc)

print(text_collection.index_information())
docs = text_collection.find({'$text': {'$search': 'java coffee shop'}})
for doc in docs:
    print(doc)

print(text_collection.index_information())
docs = text_collection.find({'$text': {'$search': '\"java \"'}})
for doc in docs:
    print(doc)

print(text_collection.index_information())
docs = text_collection.find({'$text': {'$search': 'Coffee', '$caseSensitive': True}})
for doc in docs:
    print(doc)