from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri) 
data = client.c4e
collection = data["customers"]
all_collection = list(collection.find())
events = 0
wom = 0 
ads = 0
for datas in all_collection :
    if datas['ref'] == 'events' :
        events = events + 1
    elif datas['ref'] == 'wom' :
        wom = wom + 1 
    else : 
        ads = ads + 1
#1. prepare data
machine_counts = [events,wom,ads]

#2. prepare labels
machine_names = ["events" , "wom" , "ads"]

#3. draw pie
pyplot.pie(machine_counts, labels = machine_names, autopct="%.1f%%", shadow=True, explode=(0,0.1,0.1))
pyplot.axis("equal")
#4. show
pyplot.show()
