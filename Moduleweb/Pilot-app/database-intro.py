from pymongo import MongoClient
#1 connect mongodb
mongo_uri = "mongodb+srv://admin:admin@cluster0-d3to1.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri) 

#2 get/create database 
db_demo = client.test_database 

#3 get/create collection
first_collection = db_demo["my_collection"]

#4 create document
# game_document = {
#     "title" : "auto chess",
#     "description" : "game l",
# }

#5 insert document 
# first_collection.insert_one(game_document)

#6 READ
#6.1 Read all
# all_document = first_collection.find()
# for document in all_document:
#     print(document["title"])

#6.2 Read one
one_document = first_collection.find_one({"title":"pikachu"})
print(one_document)