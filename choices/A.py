import json 
import time 
import random
sleep = time.sleep 

def choose(text, options):
    answer = input(text)
    try: 
        print("You chose: " + options[answer].lower())
        return answer 
    except: 
        print("Invalid value, try again...")
        return choose(text, options)

def battle(enemy_health, hero_health):
    won = {0, False}
    random_chance = random.randint(1,6)
    choice = choose("Choose to either RUN or FIGHT: ", {
        "RUN": "to run away, it... ",
        "FIGHT": "to attempt to fight, you... "
    })
    if choice == "RUN":
        if random_chance > 3:
            won = {1, True}
            print("was successful!\n")
        else: 
            print("was not successful")
    if choice == "FIGHT":
        if random_chance > 2: 
            won = {2, True}
            print("was successful\n")
        else:
            print("was not successful")
    return won

print("Welcome to the wonderful forest of FOREST_NAME\n")
print("FOREST_NAME includes many great things, inlcuding some of the most")
