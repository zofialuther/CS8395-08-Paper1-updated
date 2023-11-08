import random

doors = 3
iterations = 1000

def monty_hall(choice, switch=False, doorCount=doors):
    prize_door = random.randint(1, doorCount)
    if choice == prize_door:
        unpicked_doors = [x for x in range(1, doorCount+1) if x != choice]
    else:
        unpicked_doors = [x for x in range(1, doorCount+1) if x != choice and x != prize_door]
    
    alternative_door = unpicked_doors[0]
    
    if switch:
        return alternative_door
    else:
        return choice

print("Simulation of Monty Hall problem with", doors, "doors and", iterations, "iterations")

not_switching = sum(monty_hall(random.randint(1, doors), switch=False) == prize_door for _ in range(iterations))
switching = sum(monty_hall(random.randint(1, doors), switch=True) == prize_door for _ in range(iterations))

print("Results of not switching:", not_switching)
print("Results of switching:", switching)