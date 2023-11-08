```python
import random

def generate_numbers():
    return [random.randint(1, 9) for _ in range(4)]

def calculate_result(numbers, operator):
    if operator == '+':
        return numbers[0] + numbers[1]
    elif operator == '-':
        return numbers[0] - numbers[1]
    elif operator == '*':
        return numbers[0] * numbers[1]
    elif operator == '/':
        return numbers[0] / numbers[1]

def main():
    target_number = 24
    play = True
    
    while play:
        numbers = generate_numbers()
        print(f"Your numbers are: {numbers}")
        
        user_input = input("Enter your equation using +, -, *, /: ")
        result = eval(user_input)
        
        if result == target_number:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {target_number}")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            play = False

if __name__ == "__main__":
    main()
```