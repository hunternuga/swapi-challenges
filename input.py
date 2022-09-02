import requests
import yaml
import json

url_people=json.loads(requests.get("https://swapi.dev/api/people/").text)
url_planets=json.loads(requests.get("https://swapi.dev/api/planets/").text)
url_starships=json.loads(requests.get("https://swapi.dev/api/starships/").text)

with open('/Users/hnuga/Desktop/dev-ops-challenge/input.yaml') as file:
    user_list = yaml.load(file, Loader=yaml.FullLoader)
    print(json.dumps(user_list, indent=2,sort_keys=True))
