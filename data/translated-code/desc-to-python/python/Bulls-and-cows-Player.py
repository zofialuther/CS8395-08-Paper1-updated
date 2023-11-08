```python
import itertools
import random

def generate_choices():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    choices = list(itertools.permutations(digits, 4))
    random.shuffle(choices)
    return choices

def calculate_score(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(secret))
    cows -= bulls
    return bulls, cows

def play_game():
    secret = random.choice(generate_choices())
    while True:
        guess = input("Enter your guess: ")
        bulls, cows = calculate_score(secret, guess)
        print(f"{bulls} bulls, {cows} cows")
        if bulls == 4:
            print("Congratulations! You guessed the sequence!")
            break
        choices = [choice for choice in generate_choices() if calculate_score(secret, choice) == (bulls, cows)]
        if not choices:
            print(f"No choices fit the scores ({bulls} bulls, {cows} cows). The correct sequence was {secret}.")
            break

play_game()
```