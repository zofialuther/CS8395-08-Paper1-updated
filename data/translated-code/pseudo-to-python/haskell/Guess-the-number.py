import random

def main():
    random_num = random.randint(1, 10)
    gameloop(random_num)

def gameloop(random_num):
    guess = int(input("Enter your guess: "))
    if guess == random_num:
        print("You got it!")
    else:
        print("Nope. Guess again.")
        gameloop(random_num)