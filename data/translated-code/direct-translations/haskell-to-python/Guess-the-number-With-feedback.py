import random

def until_(act, pred):
    result = act
    while not pred(result):
        result = act
    return result

def answerIs(ans, guess):
    if ans < guess:
        print("Too high. Guess again.")
        return False
    elif ans == guess:
        print("You got it!")
        return True
    else:
        print("Too low. Guess again.")
        return False

def ask():
    while True:
        try:
            line = input("Enter a number: ")
            return int(line)
        except ValueError:
            print("Please enter a number.")

def main():
    ans = random.randint(1, 100)
    print("Try to guess my secret number between 1 and 100.")
    until_(ask, lambda x: answerIs(ans, x))

main()