import random

number_to_guess = random.randint(1, 10)

while True:
    user_guess = int(input("Guess the number between 1 and 10: "))
    if user_guess == number_to_guess:
        print("That's right!")
        break
    else:
        print("Incorrect, guess again.")