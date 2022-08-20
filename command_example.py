from bs4 import BeautifulSoup
import requests
import pymongo
import re

conn = pymongo.MongoClient()
actor_db = conn.cine21
actor_collection = actor_db.actor_collection

# 1. 컬럼명 변경
actor_collection.update_many({}, {'$rename' : {'학교' : '출신학교'}})

docs = actor_collection.find({}).limit(3)
print(1)
for doc in docs:
    print(doc)

# 2. find의 다양한 문법 - sort
# 역순으로 출력하고 싶을 때 pymongo.DESCENDING
docs = actor_collection.find({}).sort('생년월일', pymongo.DESCENDING).limit(10)
print(2)
for doc in docs:
    print(doc)

# 3. find의 다양한 문법 - exists
docs = actor_collection.find({'특기' : {'$exists' : True}}).sort('흥행지수').limit(5)
print(3)
for doc in docs:
    print(doc)
docs = actor_collection.find({'생년월일' : {'$exists' : False}}, {'배우이름': 1, '_id':0})
print(3)
for doc in docs:
    print(doc)

# 4. find의 다양한 문법 - 필드값 범위로 검색
docs = actor_collection.find({'흥행지수': {'$lt': 10000}},
                             {'배우이름': 1, '출연영화': 1, '_id': 0})
print(4)
for doc in docs:
    print(doc)

# 5. find의 다양한 문법 - or
docs = actor_collection.find({'$or': [{'출연영화': '한산: 용의 출현'}, {'출연영화': '명량'}]},
                             {'배우이름': 1, '출연영화': 1, '_id': 0}).sort('배우이름')
print(5)
for doc in docs:
    print(doc)

docs = actor_collection.find({'흥행지수': {'$gte': 10000},'$or': [{'출연영화': '한산: 용의 출현'}, {'출연영화': '명량'}]},
                             {'배우이름': 1, '출연영화': 1, '_id': 0}).sort('배우이름')
print(5)
for doc in docs:
    print(doc)