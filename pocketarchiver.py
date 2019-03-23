import requests
import json

searcher = {"consumer_key":"CONSUMER KEY", "access_token":"ACCESS TOKEN", "count" : "1000", "search":"DOMAIN NAME"}

r = requests.post("https://getpocket.com/v3/get", data = searcher)

r_dict = json.loads(r.text)

items = r_dict['list']

item_list = []

for k, v in items.items():
    item_list.append(k)

for item in item_list:
    r2 = requests.post('https://getpocket.com/v3/send', data={
            'consumer_key': 'CONSUMER KEY',
            'access_token': 'ACCESS TOKEN',
            'actions': json.dumps([{
                'item_id': '{}'.format(item),
                'action':'archive'
             }])
        })
