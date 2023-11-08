import random

def main():
    print("Welcome to the 24 Game!")
    digits = [random.randint(1, 9) for _ in range(4)]
    print("The randomly generated digits are:", digits)
    guessLoop(digits)

def guessLoop(digits):
    guess = input("Enter your expression guess: ")
    result = processGuess(digits, guess)
    if result == "Invalid":
        print("Invalid guess. Please try again.")
        guessLoop(digits)
    else:
        print("Correct")

def processGuess(digits, expressions):
    if not expressions:
        return ""
    elif not checkExpressionsMatch(digits, expressions):
        return "Expressions do not match the digits"
    else:
        if calc(expressions) == 24:
            return "Correct"
        else:
            return "Incorrect"

def calc(expressions):
    # Implementation of the calc function

def simplify(values, expression):
    # Implementation of the simplify function

def isOp(expression):
    # Implementation of the isOp function

# Implementation of the list of operators with their corresponding functions.