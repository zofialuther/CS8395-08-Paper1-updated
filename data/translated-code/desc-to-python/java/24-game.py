import random

def generate_sequence():
    return [random.randint(1, 9) for _ in range(4)]

def evaluate_input(user_input, sequence):
    # perform evaluation and comparison logic here
    pass

def main():
    sequence = generate_sequence()
    print("The sequence is:", sequence)
    user_input = input("Enter your expression using the 4 digits to make 24: ")
    evaluate_input(user_input, sequence)

main()