```python
import random

def pick_number(min_value, max_value):
    print(f"Please pick a number between {min_value} and {max_value}.")

def guess_number(min_value, max_value):
    guess = (min_value + max_value) // 2
    feedback = input(f"Is {guess} the correct number? (yes, too low, too high): ")
    return guess, feedback

def play():
    min_value = 1
    max_value = 100
    pick_number(min_value, max_value)
    chosen_number = int(input("Enter your chosen number: "))
    
    while True:
        guess, feedback = guess_number(min_value, max_value)
        if feedback == "yes":
            print(f"The correct number is {guess}!")
            break
        elif feedback == "too low":
            min_value = guess + 1
        else:
            max_value = guess - 1

play()
```