```python
import random

def main():
    n = random.randint(1, 10)
    print("Guess the number between 1 and 10: ")
    guess = int(input())
    while guess != n:
        print("Wrong! Guess again: ")
        guess = int(input())
    print("Well guessed!")

if __name__ == "__main__":
    main()
```