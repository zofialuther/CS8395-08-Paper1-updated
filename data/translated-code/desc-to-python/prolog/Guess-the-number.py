```python
import random

number_to_guess = random.randint(1, 10)
attempts = 0

while attempts < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number_to_guess:
        print("Well guessed!")
        print("true")
        break
    else:
        print("Try again")
        attempts += 1
```