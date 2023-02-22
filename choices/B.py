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


print("Welcome to the wonderful CASTLE of CASTLE_NAME")
print("CASTLE_NAME includes many great things, inlcuding some great friends and enemies to meet!\n")

print("Oh no! You encountered a sorcerer!")
battle()
response = input("You found a new friend!")
add_points(5)
print("Hello! My name is NAME_HERE, I am here to teach you about this place, but first\nSOLVE MY RIDDE!\nWhat is born on four legs, lives on two and is old on three?\n")
result = input("Enter your answer here: ").lower()
if result == "a human":
    print("Congratulations! You were correct.")
    add_points(10)
elif result == "human":
    print("Congratulations! You were correct.")
    add_points(10)
else:
    print("NO!! DIE!!!!!!!!!")

print("You stumbled upon an enemy! He had a question for you:\nFor how long does the average human live?")
result = input("Enter your answer here: ")
if result == "72":
    print("You won!")
    add_points(500)
else: 
    die()

print("\nYou defeated the BOSS_NAME...\nYOU WON CHOICE: A\n\nDELETING YOUR SAVE DATA...")
sleep(1)
data = {  
    "points": 0,
    "choice": None
}
json_write_data()
print("Successfully deleted save data.")
