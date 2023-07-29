import requests

# PubChem PUG REST API的基本URL
base_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug'

# 提供化合物名称或CID
compound_name = 'aspirin'

# 搜索化合物并获取CID
search_url = f'{base_url}/compound/name/{compound_name}/cids/JSON'
response = requests.get(search_url)
response_json = response.json()
print(response.json())
if 'IdentifierList' in response_json:
    cid = response_json['IdentifierList']['CID'][0]

    # 下载SDF数据
    download_url = f'{base_url}/compound/cid/{cid}/json'
    response = requests.get(download_url)

    if response.status_code == 200:
        with open(f'{compound_name}.json', 'w') as file:
            file.write(response.text)
        print('数据下载成功！')
    else:
        print('数据下载失败。')
else:
    print('未找到相关化合物。')
