import requests
import json

url = 'https://swapi.dev/api/starships'
swapi_ships = requests.get(url)

def get_pilot(pilots_url):
    p = requests.get(pilots_url)
    pilot = json.loads(p.text)
    name = pilot['name']
    return name

if swapi_ships.status_code == 200:
    swapi_s = swapi_ships.json()
    for ships in swapi_s['results']:
        print("The " + str(ships["name"]) + " is piloted by: ")
        pilots = (ships['pilots'])
        for x in range(len(pilots)):
            piloturl = pilots[x]
            print(" - " + str(get_pilot(piloturl)))
        else:
            if (str(ships["pilots"])) == "[]":
                print(" - A lot of people!")


