```python
import random

def generate_number():
    number = random.sample(range(10), 4)
    if number[0] == 0:
        number = random.sample(range(1, 10), 4)
    return ''.join(map(str, number))

def check_duplicates(number):
    return len(number) == len(set(number))

def bulls_and_cows(secret_number, guess):
    bulls = sum(1 for i in range(4) if secret_number[i] == guess[i])
    cows = sum(1 for i in range(4) if secret_number[i] != guess[i] and secret_number[i] in guess)
    return bulls, cows

def main():
    secret_number = generate_number()
    attempts = 0
    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit() or len(guess) != 4 or not check_duplicates(guess):
            print("Invalid input. Please enter a 4-digit number with no duplicate digits.")
            continue
        attempts += 1
        bulls, cows = bulls_and_cows(secret_number, guess)
        print(f"Bulls: {bulls}, Cows: {cows}")
        if bulls == 4:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
```