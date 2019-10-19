import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

APIKEY = "d8a2e073e503004a5e0b0755ab8a27ce"

headers = {
    'user-key' : APIKEY
}
url ="https://api-v3.igdb.com/games/?fields=name"
response = requests.get(url,headers=headers)


jprint(response.json())



