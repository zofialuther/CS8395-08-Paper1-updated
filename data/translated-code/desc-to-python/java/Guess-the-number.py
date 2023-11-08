import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    guessed_number = 0
    
    while guessed_number != number_to_guess:
        guessed_number = int(input("Guess the number between 1 and 10: "))
        if guessed_number != number_to_guess:
            print("Incorrect guess. Try again.")
    
    print("Congratulations! You guessed the correct number.")

number_guessing_game()