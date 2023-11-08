import random

random_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == random_number:
        print("You got it!")
        break
    else:
        print("Try again!")