import requests
from pymongo import MongoClient

# PubChem PUG REST API的基本URL
base_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug'

# 提供化合物名称或CID
compound_name = 'aspirin'

# 搜索化合物并获取CID
search_url = f'{base_url}/compound/name/{compound_name}/cids/JSON'
response = requests.get(search_url)
response_json = response.json()

if 'IdentifierList' in response_json:
    cid = response_json['IdentifierList']['CID'][0]

    # 获取化合物的详细信息
    info_url = f'{base_url}/compound/cid/{cid}/JSON'
    info_response = requests.get(info_url)
    info_json = info_response.json()


    if 'PC_Compounds' in info_json:
        compound_data = info_json['PC_Compounds'][0]

        # 在这里将化合物数据保存到MongoDB数据库
        # 连接MongoDB数据库
        client = MongoClient('mongodb://localhost:27017')

        # 选择或创建数据库
        db = client['mydatabase']

        # 选择或创建集合（表）
        collection = db['compounds']

        # 插入文档（化合物数据）
        compound_id = collection.insert_one(compound_data).inserted_id

        print('数据保存成功！')
    else:
        print('未找到相关化合物信息。')
else:
    print('未找到相关化合物。')
