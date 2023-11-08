doors, iterations = 3, 100000  # could try 100,1000

def monty_hall(choice, switch=False, doorCount=doors):
    # Set up doors
    door = [False] * doorCount
    # One door with prize
    door[randrange(doorCount)] = True

    chosen = door[choice]

    unpicked = door[:]
    del unpicked[choice]

    # Out of those unpicked, the alternative is either:
    #   the prize door, or
    #   an empty door if the initial choice is actually the prize.
    alternative = True in unpicked

    if switch:
        return alternative
    else:
        return chosen

print("\nMonty Hall problem simulation:")
print(doors, "doors,", iterations, "iterations.\n")

print("Not switching allows you to win", sum(monty_hall(randrange(3), switch=False) for x in range(iterations)),
      "out of", iterations, "times.")
print("Switching allows you to win", sum(monty_hall(randrange(3), switch=True) for x in range(iterations)),
      "out of", iterations, "times.\n")