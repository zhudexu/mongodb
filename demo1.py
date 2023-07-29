
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['example']
mycol = mydb["example"]
for x in mycol.find({},{"_id": 0, "name": 1}):
    print(x['name'])
