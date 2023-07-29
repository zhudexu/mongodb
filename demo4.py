import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["compounds"]
for x in mycol.find({}, {"_id": 0, "id": 1}):
    print(x['id']['id']['cid'])