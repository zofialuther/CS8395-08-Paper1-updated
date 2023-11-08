import random

def number_reversal_game():
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    attempts = 0
    
    while numbers != sorted(numbers):
        print(numbers)
        reverse_count = int(input("How many digits from the left do you want to reverse? "))
        numbers[:reverse_count] = reversed(numbers[:reverse_count])
        attempts += 1
    
    print(f"Congratulations! You sorted the numbers in {attempts} attempts.")

number_reversal_game()