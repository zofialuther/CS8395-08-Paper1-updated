import random

def gameloop(r):
    i = int(input())
    if i == r:
        print("You got it!")
    else:
        print("Nope. Guess again.")
        gameloop(r)

main = random.randint(1, 10)
gameloop(main)