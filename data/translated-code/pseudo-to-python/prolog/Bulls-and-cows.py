```python
import random

def bulls_and_cows_server():
    LenGuess = proposition
    Solution = [0] * LenGuess
    choose(Solution)
    while True:
        print('Your guess : ')
        Guess = input()
        if study(Solution, Guess, Bulls, Cows):
            print('Bulls :', Bulls, ' Cows :', Cows)
            if Bulls == LenGuess:
                return
            else:
                Digits = digits
                Max = Digits + 1
                print('Guess must be of', LenGuess, 'digits between 1 and', Max)
                return

def choose(Solution):
    Digits = digits
    Max = Digits + 1
    while True:
        for i in range(len(Solution)):
            Solution[i] = random.randint(1, Max)
        if len(set(Solution)) == len(Solution):
            break

def study(Solution, Guess, Bulls, Cows):
    LenGuess = proposition
    Digits = digits
    Ms = [int(x) for x in str(Guess)]
    if len(Ms) != LenGuess:
        return False
    for x in Ms:
        if x <= 0 or x > Digits + 1:
            return False
    Bulls = sum(1 for i in range(len(Solution)) if Solution[i] == Ms[i])
    TT = sum(1 for Y1 in Solution for X2 in Ms if X2 == Y1)
    Cows = TT - Bulls
    return True
```