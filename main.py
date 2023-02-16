import time 
sleep = time.sleep

options = {
    "A": "Embark on your amazing adventure in a large forest",
    "B": "Begin your adventure in an impressive ancient castle",
    "C": "Survive your way through a frozen wasteland"
}

print("Welcome! You will be able to choose between 3 options.\n")
sleep(1)
for i in options: 
    print(i + ": " + options[i])
print("\n")

def choose():
    answer = input("Please enter your answer now (A/B/C):").capitalize()
    try: 
        print("Get ready to " + options[answer].lower() + "!")
        return answer 
    except: 
        print("Invalid value, try again...")
        return choose()
found = choose()
