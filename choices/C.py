import json 
import time 
import random
sleep = time.sleep 
data = {
    "points": 0,
    "choice": "B"
}

def json_write_data():
    with open("choices\savedata.json", "w") as json_file:
        json.dump(data, json_file)
json_write_data()

def add_points(points):
    print("+" + str(points) + " points!")
    data["points"] += points
    json_write_data()
    print("Current points: " + str(data["points"]) + "\n")

def die():
    print("\nYOU DIED\n")
    sleep(.1)
    print("YOUR ADVENTURE HAS ENDED.")
    exit()

def choose(text, options):
    answer = input(text).upper()
    try: 
        print("You chose: " + options[answer].lower())
        return answer 
    except: 
        print("Invalid value, try again...")
        return choose(text, options)

def battle():
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
            print("was not successful, you died")
            die()
            
    if choice == "FIGHT":
        if random_chance > 2: 
            won = {2, True}
            print("were successful\n")
        else:
            print("were not successful, you died") 
            die()
            
    return won

