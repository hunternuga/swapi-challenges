import json
import requests

url = json.loads(requests.get('https://swapi.dev/api/people/').text)
url_2 = json.loads(requests.get('https://swapi.dev/api/people/?page=2').text)
url_3 = json.loads(requests.get('https://swapi.dev/api/people/?page=3').text)
url_4 = json.loads(requests.get('https://swapi.dev/api/people/?page=4').text)
url_5 = json.loads(requests.get('https://swapi.dev/api/people/?page=5').text)
url_6 = json.loads(requests.get('https://swapi.dev/api/people/?page=6').text)
url_7 = json.loads(requests.get('https://swapi.dev/api/people/?page=7').text)
url_8 = json.loads(requests.get('https://swapi.dev/api/people/?page=8').text)
url_9 = json.loads(requests.get('https://swapi.dev/api/people/?page=9').text)
#Urls to pull data down from 2 pages worth of people data in Swapi.