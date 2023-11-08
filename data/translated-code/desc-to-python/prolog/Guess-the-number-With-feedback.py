```python
user_guess = input("Guess an integer between 1 and 10: ")

try:
    user_guess = int(user_guess)
    if user_guess < 1 or user_guess > 10:
        print("Invalid input.")
    else:
        if user_guess < target_number:
            print("Your guess is too low.")
except ValueError:
    print("Invalid input.")
```