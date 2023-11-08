import random

def guessing_game():
    target_number = random.randint(1, 100)
    while True:
        guess = input("Guess the number between 1 and 100: ")
        if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
            print("Please enter a valid number within the specified range.")
        else:
            if int(guess) == target_number:
                print("Congratulations! You guessed the correct number.")
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() == "yes":
                    guessing_game()
                else:
                    break
            else:
                print("Try again!")