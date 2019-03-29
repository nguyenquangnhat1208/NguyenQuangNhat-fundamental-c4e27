from pymongo import MongoClient
from faker import Faker
from random import randint,choice
faker = Faker()

mongo_uri = "mongodb+srv://admin:admin@cluster0-d3to1.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri) 

pilot_app = client.db_pilot

Services = pilot_app["services"]
# for i in range(50):
#     new_services = {
#         "name" : faker.name(),
#         "age" : randint(18,30),
#         "gender" : choice(["male","female"]),
#         "height" : randint(150,190),
#         "available" : choice([True,False]),
#         "address" : faker.address(),
#     }
#     services.insert_one(new_services)
#     print("saving document {0}.....".format(i+1))
