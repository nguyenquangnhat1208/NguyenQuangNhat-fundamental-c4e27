from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb+srv://admin:admin@cluster0-d3to1.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri) 

bikedata = client.db_bike

bike_collection = bikedata["my_data_bike"]