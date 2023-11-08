```python
import random

def generate_combinations():
    return [str(i) + str(j) + str(k) + str(l) for i in range(1, 10) for j in range(1, 10) 
            for k in range(1, 10) for l in range(1, 10) if len(set([i, j, k, l])) == 4]

def make_guess(combinations):
    return random.choice(combinations)

def get_bulls_and_cows(guess, answer):
    bulls = sum(1 for i in range(4) if guess[i] == answer[i])
    cows = sum(1 for i in range(4) if guess[i] in answer and guess[i] != answer[i])
    return bulls, cows

def filter_combinations(combinations, guess, bulls, cows):
    return [combo for combo in combinations if get_bulls_and_cows(guess, combo) == (bulls, cows)]

def main():
    combinations = generate_combinations()
    while len(combinations) > 1:
        guess = make_guess(combinations)
        print("Guess:", guess)
        bulls = int(input("Bulls: "))
        cows = int(input("Cows: "))
        combinations = filter_combinations(combinations, guess, bulls, cows)
    print("The correct combination is:", combinations[0])

if __name__ == "__main__":
    main()
```