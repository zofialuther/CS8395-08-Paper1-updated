```python
import random

secret_number = random.randint(1, 100)

while True:
    user_input = input("Guess the secret number between 1 and 100: ")
    
    if user_input.isdigit():
        guess = int(user_input)
        
        if guess == secret_number:
            print("You got it!")
            break
        elif guess < secret_number:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")
    else:
        print("Please enter a valid number.")
```