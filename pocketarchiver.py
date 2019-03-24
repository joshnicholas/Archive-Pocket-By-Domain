import requests
import json

searcher = {"consumer_key":"CONSUMER KEY", "access_token":"ACCESS TOKEN", "count" : "1000", "domain":"DOMAIN NAME"}

r = requests.post("https://getpocket.com/v3/get", data = searcher)

r_dict = json.loads(r.text)

# look up individual article ids

items = r_dict['list']

item_list = []

# create a list of article ids to iterate through

for k, v in items.items():
    item_list.append(k)

# delete all the articles corresponding to the articles in the list

for item in item_list:
    r2 = requests.post('https://getpocket.com/v3/send', data = {
            'consumer_key': 'CONSUMER KEY',
            'access_token': 'ACCESS TOKEN',
            'actions': json.dumps([{
                'item_id': '{}'.format(item),
                'action':'archive'
             }])
        })
