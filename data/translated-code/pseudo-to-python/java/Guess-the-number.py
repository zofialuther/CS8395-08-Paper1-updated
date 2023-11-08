import random

n = random.randint(1, 10)
print("Guess the number between 1 and 10: ")
guess = int(input())

while guess != n:
    print("Wrong! Guess again: ")
    guess = int(input())

print("Well guessed!")