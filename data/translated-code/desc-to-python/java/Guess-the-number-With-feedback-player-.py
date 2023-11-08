```python
def guessing_game():
    low = 0
    high = 100
    user_response = ''
    
    while user_response != 'C':
        guess = (low + high) // 2
        print("Is your number", guess, "? (L/H/C)")
        user_response = input().upper()
        
        if user_response == 'L':
            low = guess + 1
        elif user_response == 'H':
            high = guess
        elif user_response == 'C':
            print("I guessed it! It's", guess)
        else:
            print("Invalid input. Please enter 'L', 'H', or 'C'.")
```