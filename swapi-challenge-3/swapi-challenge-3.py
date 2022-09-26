from url_swapi import *
import json
import argparse
import requests

# Added help argument to assist with input specifications.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To search, type the name of someone from Star Wars! (Not Case Sensitive)")
    args = parser.parse_args()

# Asks user to name a Star Wars Character
ask_user = input("Please type the full name of a Star Wars Character or Droid (Movies 1 - 6): ")
ask_user = ask_user.lower()

# Contains 9 'for' loops for each page of users from swapi.dev/api/people.
# URL pulling data are stored in the url_swapi.py file under same directory

# 1st page of users
for person_1 in url['results']:
    name = (person_1['name'])
    name = name.lower()
    if str(ask_user) == name:
        print(f'Found '+str(ask_user)+f'!')
        person_bio = input(f'Would you like to display ' + str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
        person_bio = person_bio.lower()
        if person_bio == "Y".lower():
            print(f'Printing in JSON... \n\n "bio": [')
            print(" \t{")
            print(json.dumps(f'name: ' + str(ask_user), indent=6))
            print(json.dumps(f'height: ' + str(person_1['height']), indent=6,))
            print(json.dumps(f'weight: ' + str(person_1['mass']), indent=6))
            print(json.dumps(f'gender: ' + str(person_1['gender']), indent=6))
            print(json.dumps(f'hair_color: ' + str(person_1['hair_color']), indent=6))
            print(json.dumps(f'skin_color: ' + str(person_1['skin_color']), indent=6))
            print(json.dumps(f'eye_color: ' + str(person_1['eye_color']), indent=6))
            print(json.dumps(f'birth_year: ' + str(person_1['birth_year']), indent=6))
            print(" \t}")
            print(" \t\t]")
            exit()
        else:
            if person_bio == "N".lower():
                print("Not printing person's bio...")
            exit()

# 2nd page of users
    if str(ask_user) != (person_1['name']):
        for person_2 in url_2['results']:
            name_2 = (person_2['name'])
            name_2 = name_2.lower()
            if str(ask_user) == name_2:
                print(f'Found '+str(ask_user)+f'!')
                person_bio_2 = input(f'Would you like to display '+str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
                person_bio_2 = person_bio_2.lower()
                if person_bio_2 == "Y".lower():
                    print(f'Printing... \n\n "bio": [')
                    print(" \t{")
                    print(json.dumps(f'name: ' + str(ask_user), indent=4))
                    print(json.dumps(f'height: ' + str(person_2['height']), indent=4))
                    print(json.dumps(f'weight: ' + str(person_2['mass']), indent=4))
                    print(json.dumps(f'gender: ' + str(person_2['gender']), indent=4))
                    print(json.dumps(f'hair_color: ' + str(person_2['hair_color']), indent=4))
                    print(json.dumps('skin_color: ' + str(person_2['skin_color']), indent=4))
                    print(json.dumps(f'eye_color: ' + str(person_2['eye_color']), indent=4))
                    print(json.dumps(f'birth_year: ' + str(person_2['birth_year']), indent=4))
                    print(" \t}")
                    print(" \t\t]")
                    exit()
                else:
                    if person_bio_2 == "N".lower():
                        print("Not printing person's bio...")
                    exit()

# 3rd page of users
    if str(ask_user) != (person_2['name']):
        for person_3 in url_3['results']:
            name_3 = (person_3['name'])
            name_3 = name_3.lower()
            if str(ask_user) == name_3:
                print(f'Found ' + str(ask_user) + f'!')
                person_bio_3 = input(f'Would you like to display ' + str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
                person_bio_3 = person_bio_3.lower()
                if person_bio_3 == "Y".lower():
                    print(f'Printing... \n\n "bio": [')
                    print(" \t{")
                    print(json.dumps(f'name: ' + str(ask_user), indent=4))
                    print(json.dumps(f'height: ' + str(person_3['height']), indent=4))
                    print(json.dumps(f'weight: ' + str(person_3['mass']), indent=4))
                    print(json.dumps(f'gender: ' + str(person_3['gender']), indent=4))
                    print(json.dumps(f'hair_color: ' + str(person_3['hair_color']), indent=4))
                    print(json.dumps('skin_color: ' + str(person_3['skin_color']), indent=4))
                    print(json.dumps(f'eye_color: ' + str(person_3['eye_color']), indent=4))
                    print(json.dumps(f'birth_year: ' + str(person_3['birth_year']), indent=4))
                    print(" \t}")
                    print(" \t\t]")
                    exit()
                else:
                    if person_bio_3 == "N".lower():
                        print("Not printing person's bio...")
                    exit()

# 4th page of users
    if str(ask_user) != (person_3['name']):
        for person_4 in url_4['results']:
            name_4 = (person_4['name'])
            name_4 = name_4.lower()
            if str(ask_user) == name_4:
                print(f'Found '+str(ask_user)+f'!')
                person_bio_4 = input(f'Would you like to display ' + str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
                person_bio_4 = person_bio_4.lower()
                if person_bio_4 == "Y".lower():
                    print(f'Printing... \n\n "bio": [')
                    print(" \t{")
                    print(json.dumps(f'name: ' + str(ask_user), indent=4))
                    print(json.dumps(f'height: ' + str(person_4['height']), indent=4))
                    print(json.dumps(f'weight: ' + str(person_4['mass']), indent=4))
                    print(json.dumps(f'gender: ' + str(person_4['gender']), indent=4))
                    print(json.dumps(f'hair_color: ' + str(person_4['hair_color']), indent=4))
                    print(json.dumps('skin_color: ' + str(person_4['skin_color']), indent=4))
                    print(json.dumps(f'eye_color: ' + str(person_4['eye_color']), indent=4))
                    print(json.dumps(f'birth_year: ' + str(person_4['birth_year']), indent=4))
                    print(" \t}")
                    print(" \t\t]")
                    exit()
                else:
                    if person_bio_4 == "N".lower():
                        print("Not printing person's bio...")
                    exit()

# 5th page of users
    if str(ask_user) != (person_4['name']):
        for person_5 in url_5['results']:
            name_5 = (person_5['name'])
            name_5 = name_5.lower()
            if str(ask_user) == name_5:
                print(f'Found '+str(ask_user)+f'!')
                person_bio_5 = input(f'Would you like to display ' + str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
                person_bio_5 = person_bio_5.lower()
                if person_bio_5 == "Y".lower():
                    print(f'Printing... \n\n "bio": [')
                    print(" \t{")
                    print(json.dumps(f'name: ' + str(ask_user), indent=4))
                    print(json.dumps(f'height: ' + str(person_5['height']), indent=4))
                    print(json.dumps(f'weight: ' + str(person_5['mass']), indent=4))
                    print(json.dumps(f'gender: ' + str(person_5['gender']), indent=4))
                    print(json.dumps(f'hair_color: ' + str(person_5['hair_color']), indent=4))
                    print(json.dumps('skin_color: ' + str(person_5['skin_color']), indent=4))
                    print(json.dumps(f'eye_color: ' + str(person_5['eye_color']), indent=4))
                    print(json.dumps(f'birth_year: ' + str(person_5['birth_year']), indent=4))
                    print(" \t}")
                    print(" \t\t]")
                    exit()
                else:
                    if person_bio_5 == "N".lower():
                        print("Not printing person's bio...")
                    exit()

# 6th page of users
    if str(ask_user) != (person_5['name']):
        for person_6 in url_6['results']:
            name_6 = (person_6['name'])
            name_6 = name_6.lower()
            if str(ask_user) == name_6:
                print(f'Found '+str(ask_user)+f'!')
                person_bio_6 = input(f'Would you like to display ' + str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
                person_bio_6 = person_bio_6.lower()
                if person_bio_6 == "Y".lower():
                    print(f'Printing... \n\n "bio": [')
                    print(" \t{")
                    print(json.dumps(f'name: ' + str(ask_user), indent=4))
                    print(json.dumps(f'height: ' + str(person_6['height']), indent=4))
                    print(json.dumps(f'weight: ' + str(person_6['mass']), indent=4))
                    print(json.dumps(f'gender: ' + str(person_6['gender']), indent=4))
                    print(json.dumps(f'hair_color: ' + str(person_6['hair_color']), indent=4))
                    print(json.dumps('skin_color: ' + str(person_6['skin_color']), indent=4))
                    print(json.dumps(f'birth_year: ' + str(person_6['birth_year']), indent=4))
                    print(" \t}")
                    print(" \t\t]")
                    exit()
                else:
                    if person_bio_6 == "N".lower():
                        print("Not printing person's bio...")
                    exit()

# 7th page of users
    if str(ask_user) != (person_6['name']):
        for person_7 in url_7['results']:
            name_7 = (person_7['name'])
            name_7 = name_7.lower()
            if str(ask_user) == name_7:
                print(f'Found '+str(ask_user)+f'!')
                person_bio_7 = input(f'Would you like to display ' + str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
                person_bio_7 = person_bio_7.lower()
                if person_bio_7 == "Y".lower():
                    print(f'Printing... \n\n "bio": [')
                    print(" \t{")
                    print(json.dumps(f'name: ' + str(ask_user), indent=4))
                    print(json.dumps(f'height: ' + str(person_7['height']), indent=4))
                    print(json.dumps(f'weight: ' + str(person_7['mass']), indent=4))
                    print(json.dumps(f'gender: ' + str(person_7['gender']), indent=4))
                    print(json.dumps(f'hair_color: ' + str(person_7['hair_color']), indent=4))
                    print(json.dumps('skin_color: ' + str(person_7['skin_color']), indent=4))
                    print(json.dumps(f'birth_year: ' + str(person_7['birth_year']), indent=4))
                    print(" \t}")
                    print(" \t\t]")
                    exit()
                else:
                    if person_bio_7 == "N".lower():
                        print("Not printing person's bio...")
                    exit()

# 8th page of users
    if str(ask_user) != (person_7['name']):
        for person_8 in url_8['results']:
            name_8 = (person_8['name'])
            name_8 = name_8.lower()
            if str(ask_user) == name_8:
                print(f'Found '+str(ask_user)+f'!')
                person_bio_8 = input(f'Would you like to display ' + str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
                person_bio_8 = person_bio_8.lower()
                if person_bio_8 == "Y".lower():
                    print(f'Printing... \n\n "bio": [')
                    print(" \t{")
                    print(json.dumps(f'name: ' + str(ask_user), indent=4))
                    print(json.dumps(f'height: ' + str(person_8['height']), indent=4))
                    print(json.dumps(f'weight: ' + str(person_8['mass']), indent=4))
                    print(json.dumps(f'gender: ' + str(person_8['gender']), indent=4))
                    print(json.dumps(f'hair_color: ' + str(person_8['hair_color']), indent=4))
                    print(json.dumps('skin_color: ' + str(person_8['skin_color']), indent=4))
                    print(json.dumps(f'birth_year: ' + str(person_8['birth_year']), indent=4))
                    print(" \t}")
                    print(" \t\t]")
                    exit()
                else:
                    if person_bio_8 == "N".lower():
                        print("Not printing person's bio...")
                    exit()

# 9th page of users
    if str(ask_user) != (person_8['name']):
        for person_9 in url_9['results']:
            name_9 = (person_9['name'])
            name_9 = name_9.lower()
            if str(ask_user) == name_9:
                print(f'Found '+str(ask_user)+f'!')
                person_bio_9 = input(f'Would you like to display ' + str(ask_user) + "'s bio? \n (Y)es or (N)o: ")
                person_bio_9 = person_bio_9.lower()
                if person_bio_9 == "Y".lower():
                    print(f'Printing... \n\n "bio": [')
                    print(" \t{")
                    print(json.dumps(f'name: ' + str(ask_user), indent=4))
                    print(json.dumps(f'height: ' + str(person_9['height']), indent=4))
                    print(json.dumps(f'weight: ' + str(person_9['mass']), indent=4))
                    print(json.dumps(f'gender: ' + str(person_9['gender']), indent=4))
                    print(json.dumps(f'hair_color: ' + str(person_9['hair_color']), indent=4))
                    print(json.dumps('skin_color: ' + str(person_9['skin_color']), indent=4))
                    print(json.dumps(f'birth_year: ' + str(person_9['birth_year']), indent=4))
                    print(" \t}")
                    print(" \t\t]")
                    exit()
                else:
                    if person_bio_9 == "N".lower():
                        print("Not printing person's bio...")
                    exit()
