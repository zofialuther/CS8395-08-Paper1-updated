import random

def play():
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    do_turn(numbers)

def do_turn(numbers):
    print("Current list:", numbers)
    flips = int(input("Enter the number of elements to flip: "))
    # modify the list according to the input
    sorted_list = sorted(numbers)
    if numbers == sorted_list:
        print("Congratulations! You sorted the list:", numbers)
    else:
        do_turn(numbers)