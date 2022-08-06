import pymongo
conn = pymongo.MongoClient()
books = conn.books
it_books = books.it_books

data = list()
for i in range(100):
    data.append({'author': 'Dave Lee', 'publisher': 'fffffggg', 'number': i})

# CRUD - Create(Insert)
it_books.insert_many(data)

# CRUD - Read
docs = it_books.find()
for d in docs:
    print(d)

# CRUD - Update
it_books.update_many({}, {'$set': {'publisher': 'www.naver.com'}})

# CRUD - Delete
it_books.delete_many({'number': {'$gt': 5}})
