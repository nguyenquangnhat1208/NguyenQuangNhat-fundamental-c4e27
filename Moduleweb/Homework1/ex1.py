from pymongo import MongoClient
#1 connect mongodb
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri) 
demo = client.c4e
first_poem = demo['posts']
new_poem = {
    "title" : "Hello Anh Em",
    "author" : "Nguyễn Quang Nhật",
    "content" : "Chào Anh Em"
}
first_poem.insert_one(new_poem)
