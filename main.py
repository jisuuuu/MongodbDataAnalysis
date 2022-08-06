import pymongo
connection = pymongo.MongoClient('localhost', 27017)
# connection = pymongo.MongoClient('mongodb://13.209.140.30', 12354)
knowledge = connection.knowledge
print(knowledge)

knowledge_it = knowledge.it
# knowledge_it = knowledge['it']
print(knowledge_it)

# post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"] }
# knowledge_it.insert_one(post)
# knowledge_it.insert_one({"author": "Jisu", "age": 27})

knowledge_it.insert_many(
    [
        { "author":"Dave Ahn", "age":25 },
        { "author":"Dave", "age":35 }
    ]
)