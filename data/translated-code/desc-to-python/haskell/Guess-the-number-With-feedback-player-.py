```python
import random

def number_guessing_game():
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the number range: "))
            upper_bound = int(input("Enter the upper bound of the number range: "))
            secret_number = random.randint(lower_bound, upper_bound)
            while True:
                guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You guessed the correct number.")
                    break
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please try again.")
```