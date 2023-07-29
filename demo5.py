import requests

def autocomplete_search(query,num):
    base_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/autocomplete'

    # 构造自动完成搜索URL
    #https://pubchem.ncbi.nlm.nih.gov/rest/autocomplete/compound/aspirin/json?limit=6
    autocomplete_url = f'{base_url}/compound/{query}/JSON?limit={num}'
    response = requests.get(autocomplete_url)
    response_json = response.json()
    print(response_json)

    if 'dictionary_terms' in response_json:
        information_list = response_json['dictionary_terms']['compound']

        # 提取自动完成搜索结果
        results = information_list

        return results
    else:
        return []

# 测试自动完成搜索服务
search_query = 'aspirin'
search_results = autocomplete_search(search_query,6)

if len(search_results) > 0:
    print(f'自动完成搜索结果：{search_results}')
else:
    print('未找到相关结果。')
