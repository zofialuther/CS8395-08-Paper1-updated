from Data.List import partition, intersect, nub
import Control.Monad
from random import randint

numberOfDigits = 4

def bullsAndCows():
    digits = ''.join([str(randint(1, 9)) for _ in range(numberOfDigits)])
    print("Guess away!")
    loop(digits)

def loop(digits):
    input = input()
    if okay(input):
        bulls, cows = score(digits, input)
        if bulls == numberOfDigits:
            print("You win!")
        else:
            print(f"{bulls} bulls, {cows} cows.")
            loop(digits)
    else:
        print("Malformed guess; try again.")
        loop(digits)

def okay(input):
    return len(input) == numberOfDigits and len(set(input)) == numberOfDigits and all(['1' <= c <= '9' for c in input])

def score(secret, guess):
    bulls = sum([1 for s, g in zip(secret, guess) if s == g])
    nonbulls = [(s, g) for s, g in zip(secret, guess) if s != g]
    cows = len(set(secret) & set(guess)) - bulls
    return bulls, cows

def pick(n, l, g):
    def f(n, l, g, max, ps):
        if n == 0:
            return ps, g
        else:
            i = randint(0, max)
            g = randint(0, max)
            left = l[:i]
            picked = l[i]
            right = l[i+1:]
            return f(n-1, left + right, g, max-1, [picked] + ps)
    return f(n, l, g, len(l) - 1, [])

bullsAndCows()