import pymongo

conn = pymongo.MongoClient()
actor_db = conn.cine21
actor_collection = actor_db.actor_collection

docs = actor_collection.find({'$nor' : [{'흥행지수': {'$in': [9182, 8439]}}, {'흥행지수': {'$gt': 10000}}]},
                             {'배우이름': 1, '흥행지수': 1, '_id': 0}).limit(3)
for doc in docs:
    print(doc)