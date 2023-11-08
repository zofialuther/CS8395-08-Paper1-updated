import random

def pick(n, lst):
    return random.sample(lst, n)

def bulls_and_cows():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_sequence = pick(4, digits)
    while True:
        guess = input("Enter your guess: ")
        guess_sequence = [int(x) for x in guess]
        bulls = sum(1 for i in range(4) if guess_sequence[i] == secret_sequence[i])
        cows = sum(1 for x in guess_sequence if x in secret_sequence) - bulls
        print(f"{bulls} bulls, {cows} cows")
        if bulls == 4:
            print("Congratulations, you guessed the sequence!")
            break

bulls_and_cows()