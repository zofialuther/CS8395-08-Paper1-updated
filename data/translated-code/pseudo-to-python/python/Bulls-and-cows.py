import random

def generateNumber():
    digits = '123456789'
    size = 4
    chosen = ''.join(random.sample(digits, size))
    return chosen

def playGame():
    chosen = generateNumber()
    guesses = 0
    while True:
        guesses += 1
        while True:
            guess = input("Enter your guess: ")
            if len(guess) == 4 and all(char in '123456789' for char in guess) and len(set(guess)) == 4:
                break
            else:
                print("Problem, try again. You need to enter 4 unique digits from 1 to 9")
        if guess == chosen:
            print("Congratulations you guessed correctly in", guesses, "attempts")
            break
        else:
            bulls = 0
            cows = 0
            for i in range(4):
                if guess[i] == chosen[i]:
                    bulls += 1
                elif guess[i] in chosen:
                    cows += 1
            print(bulls, "Bulls")
            print(cows, "Cows")