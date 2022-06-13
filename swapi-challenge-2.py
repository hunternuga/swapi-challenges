import requests
import json

url = json.loads(requests.get('https://swapi.dev/api/films').text)
url_pilots = json.loads(requests.get('https://swapi.dev/api/starships').text)
#URL to gather information from Swapi.
print('  {\n\t"films": [\n\t  { ')
#Prints beginning array of "ships".

for films in url['results']:
    url_films = films['title']
    print("\t\t"+'"title: "'+json.dumps(url_films, indent=4)+", ")
    print("\t\t"+'"ships": [')
    for starships in films['starships']:
        starship_url = json.loads(requests.get(starships).text)
        print('\t\t\t{"name": '+starship_url['name']+'\"},')
    print('\t\t\t ]')
    print('\t\t },')
print('  \n\t  ]')
print('  }')
