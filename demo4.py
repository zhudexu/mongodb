import pymongo
import requests
# def name(cid):
#     # https: // pubchem.ncbi.nlm.nih.gov / rest / pug / substance / sid / 10000 / synonyms / XML
#     search_url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/synonyms/json'
#     response = requests.get(search_url)
#     json = response.json()
#     return json['InformationList']['Information']['Synonym'][0]

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["compounds"]
for x in mycol.find({}, {"_id": 0, "id": 1}):
    print(x['id']['id']['cid'])
