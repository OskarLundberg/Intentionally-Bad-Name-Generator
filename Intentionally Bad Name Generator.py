import time
import random
import os


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


# approx 44.4% chance of crashing
def counting():
    problem = False
    for num in range(1, 101):
        clear()
        print("picking one of all the possible names")
        print("Loading... " + str(num) + " %")
        load_time = random.randint(1, 9) / 10
        if load_time == 0.9:
            if random.randint(1, 100) >= 50:
                load_time = random.randint(1, 9)
                if random.randint(1, 100) >= 92:
                    problem = True
                    break
        time.sleep(load_time)

    return problem


error_msg = "Stupid answer, try again bitch!\n"

print("*"*50 + "\n")
print(" "*8 + "Welcome to Random Name Generator\n")
print("*"*50 + "\n")


try:
    answer = int(input("Choose a number between 1-10: "))
except ValueError:
    answer = 666


while not 1 <= answer <= 10:
    clear()
    print(error_msg)
    try:
        answer = int(input("Choose a number between 1-10: "))
    except ValueError:
        pass

problem = True
while problem:
    problem = counting()
    if problem:
        clear()
        print("Stupid Problem Occurred")
        input("Press 'Enter' to restart Loading: ")




print("Done!\n")

time.sleep(1.5)
print("Random Name: Bob\n")
input("Press 'Enter' to exit")