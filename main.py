import time 
import json
sleep = time.sleep

options = {
    "A": "Embark on your amazing adventure in a large forest",
    "B": "Begin your adventure in an impressive ancient castle",
    "C": "Survive your way through a frozen wasteland"
}

with open("choices\savedata.json", "r") as json_file:
    data = json.load(json_file)
if data['choice']:
    exec(open("choices/" + data['choice'] + ".py").read())
else:
    print("Welcome! You will be able to choose between 3 options.\nHowever, you may not change your answer until you complete said level.\n")
    sleep(1)
    for i in options: 
        print(i + ": " + options[i])
    print("\n")

    def choose():
        answer = input("Please enter your answer now (A/B/C): ").capitalize()
        try: 
            print("Get ready to " + options[answer].lower() + "!\n")
            return answer 
        except: 
            print("Invalid value, try again...")
            return choose()
    choice = choose()
    exec(open("choices/" + choice + ".py").read())
