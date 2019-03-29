from pymongo import MongoClient
from bson.objectid import ObjectId
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
# one_document = first_collection.find_one({"title":"pikachu"})
# print(one_document)

#7. DELETE 
# delete_document = first_collection.find_one({"_id": ObjectId("5c979c96bfac141f543d8269")})
# if delete_document is not None :
#     first_collection.delete_one(delete_document)
#     print("Deleted Complete!")
# else :
#     print("Not found")

#8. Update
update_document = first_collection.find_one({"_id" : ObjectId("5c9ce241bfac14033878175c")})
new_value = { "$set": { "title" : "KHONG BIET" } }
first_collection.update_one(update_document, new_value)
