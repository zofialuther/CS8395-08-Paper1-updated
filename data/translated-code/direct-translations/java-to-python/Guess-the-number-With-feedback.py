import random

from_num = 1
to_num = 100
random_number = random.randint(from_num, to_num)
guessed_number = 0

print(f"The number is between {from_num} and {to_num}.")

while guessed_number != random_number:
    guessed_number = int(input("Guess what the number is: "))
    if guessed_number > random_number:
        print("Your guess is too high!")
    elif guessed_number < random_number:
        print("Your guess is too low!")
    else:
        print("You got it!")