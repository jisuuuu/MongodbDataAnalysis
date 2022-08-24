import pymongo

conn = pymongo.MongoClient()
actor_db = conn.cine21
actor_collection = actor_db.actor_collection

# 실습1
docs = actor_collection.find({'$nor' : [{'흥행지수': {'$in': [9182, 8439]}}, {'흥행지수': {'$gt': 10000}}]},
                             {'배우이름': 1, '흥행지수': 1, '_id': 0}).limit(3)
for doc in docs:
    print(doc)

# 실습2
docs = actor_collection.find({'직업': '가수'}).sort('흥행지수', pymongo.DESCENDING).limit(10)
for doc in docs:
    print(doc)

# 실습3
docs = actor_collection.find({'출연영화': '한산: 용의 출현'}).sort('흥행지수', pymongo.DESCENDING)
for doc in docs:
    print(doc)