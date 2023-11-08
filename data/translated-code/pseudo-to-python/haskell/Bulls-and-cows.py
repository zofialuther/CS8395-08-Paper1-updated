from random import randint

numberOfDigits = 4

def bullsAndCows():
    digits = ''.join([str(randint(1, 9)) for _ in range(numberOfDigits)])
    print("Guess away!")
    loop(digits)

def loop(digits):
    input_guess = input()
    if okay(input_guess):
        bulls, cows = score(digits, input_guess)
        if bulls == numberOfDigits:
            print("You win!")
        else:
            print(f"{bulls} bulls, {cows} cows.")
            loop(digits)
    else:
        print("Malformed guess; try again.")
        loop(digits)

def okay(input_guess):
    return len(input_guess) == numberOfDigits and len(input_guess) == len(set(input_guess)) and all('1' <= c <= '9' for c in input_guess)

def score(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(min(secret.count(char), guess.count(char)) for char in set(secret) & set(guess)) - bulls
    return bulls, cows

bullsAndCows()