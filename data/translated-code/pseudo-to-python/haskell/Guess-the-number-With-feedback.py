import random

def until_(act, pred):
    result = act
    while not pred(result):
        result = act
    return result

def answerIs(ans, guess):
    comparison = compare(ans, guess)
    if comparison == "LT":
        print("Too high. Guess again.")
        return False
    elif comparison == "EQ":
        print("You got it!")
        return True
    else:
        print("Too low. Guess again.")
        return False

def ask():
    while True:
        line = input()
        try:
            num = int(line)
            return num
        except ValueError:
            print("Please enter a number.")

def main():
    ans = random.randint(1, 100)
    print("Try to guess my secret number between 1 and 100.")
    return until_(ask(), lambda x: answerIs(ans, x))