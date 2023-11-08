```python
import random

# Game parameters
guess_length = 4
num_digits = 10

# Generate random solution
solution = ''.join(random.sample([str(i) for i in range(num_digits)], guess_length))

# Function to check guess
def check_guess(guess, solution):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            bulls += 1
        elif guess[i] in solution:
            cows += 1
    return bulls, cows

# Main game loop
while True:
    guess = input("Make a guess: ")
    if len(guess) != guess_length or not guess.isdigit():
        print("Invalid guess. Please enter a {}-digit number.".format(guess_length))
        continue
    bulls, cows = check_guess(guess, solution)
    print("Bulls: {}, Cows: {}".format(bulls, cows))
    if bulls == guess_length:
        print("Congratulations! You guessed the correct solution: {}".format(solution))
        break
```