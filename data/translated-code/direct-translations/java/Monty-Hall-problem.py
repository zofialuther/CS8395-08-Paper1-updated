import random

def main():
    switchWins = 0
    stayWins = 0
    for plays in range(32768):
        doors = [0, 0, 0]  # 0 is a goat, 1 is a car
        doors[random.randint(0, 2)] = 1  # put a winner in a random door
        choice = random.randint(0, 2)  # pick a door, any door
        shown = None  # the shown door
        while True:
            shown = random.randint(0, 2)
            if doors[shown] != 1 and shown != choice:
                break
        stayWins += doors[choice]  # if you won by staying, count it
        switchWins += doors[3 - choice - shown]
    print("Switching wins " + str(switchWins) + " times.")
    print("Staying wins " + str(stayWins) + " times.")

main()