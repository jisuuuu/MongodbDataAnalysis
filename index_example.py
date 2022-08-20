from bs4 import BeautifulSoup
import requests
import pymongo
import re

conn = pymongo.MongoClient()
actor_db = conn.cine21
actor_collection = actor_db.actor_collection

actor_collection.find_one({})
docs = actor_collection.find({}).limit(3)
for doc in docs:
    print (doc)
actor = actor_collection

# Single 필드 인덱스
# print(actor.create_index('배우이름'))
actor.drop_indexes()
# actor.drop_index([('배우이름', 1)])

# docs = actor.find({'배우이름': '손석구'})
# for doc in docs:
#     print(doc)
#
# actor.create_index([('출연영화', 'text')])
# print(actor.index_information())
#
# docs = actor.find({'$text': {'$search': '한산'}})
# for doc in docs:
#     print(doc)

# actor.create_index([('출연영화', 'text')])
# print(actor.index_information())
#
# docs = actor.find({'$text': {'$search': '한산'}})
# for doc in docs:
#     print(doc)

actor.create_index([('출연영화', pymongo.TEXT), ('직업', pymongo.TEXT)
                    , ('흥행지수', pymongo.TEXT)])
docs = actor.find({'$text': {'$search': '한'}})
for doc in docs:
    print(doc)