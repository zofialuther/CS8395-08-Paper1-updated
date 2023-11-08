```python
import random

def generate_numbers():
    return [random.randint(1, 9) for _ in range(4)]

def generate_operators():
    return ['+', '-', '*', '/']

def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return None

def main():
    print("Welcome to the 24 Game!")
    while True:
        numbers = generate_numbers()
        operators = generate_operators()
        print("Your numbers are:", numbers)
        print("Your operators are:", operators)
        expression = input("Enter an expression using the numbers and operators to equal 24 (e.g. 1 + 2 * 3 - 4): ")
        result = calculate(expression)
        if result == 24:
            print("Congratulations! You got 24!")
            break
        elif result is not None:
            print("Sorry, that's not 24. Try again!")
        else:
            print("Invalid expression. Please enter a valid expression.")
        choice = input("Press q to quit or any other key to play again: ")
        if choice.lower() == 'q':
            break

if __name__ == "__main__":
    main()
```