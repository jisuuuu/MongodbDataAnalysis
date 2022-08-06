import pymongo
connection = pymongo.MongoClient('localhost', 27017)
# connection = pymongo.MongoClient('mongodb://13.209.140.30', 12354)
knowledge = connection.knowledge
print(knowledge)

knowledge_it = knowledge.it
# knowledge_it = knowledge['it']
print(knowledge_it)

post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"] }
knowledge_it.insert_one(post)
knowledge_it.insert_one({"author": "Jisu", "age": 27})
knowledge_it.insert_many(
    [
        { "author":"Dave Ahn", "age":25 },
        { "author":"Dave", "age":35 }
    ]
)

post = {"author": "Dave", "text": "My first blog post!"}
post_id = knowledge_it.insert_one(post)

print(post_id.inserted_id) #pymongo3.7 부터는 count() 사용X estimated_document_count() 사용O

# 리스트, 객체 삽입 가능
knowledge_it.insert_one({'title' : '암살', 'castings' : ['이정재', '전지현', '하정우']})
knowledge_it.insert_one(
    {
        'title' : '실미도',
        'castings' : ['설경구', '안성기'],
        'datetime' :
        {
            'year' : '2003',
            'month' : 3,
            'val' :
            {
                'a' :
                {
                    'b' : 1
                }
            }
        }
    }
)

data = list()
data.append({'name' : 'aaron', 'age' : 20})
data.append({'name' : 'bob', 'age' : 30})
data.append({'name' : 'cathy', 'age' : 25})
data.append({'name' : 'david', 'age' : 27})
data.append({'name' : 'erick', 'age' : 28})
data.append({'name' : 'fox', 'age' : 32})
data.append({'name' : 'hmm'})

knowledge_it.insert_many(data)
print(knowledge_it.estimated_document_count())