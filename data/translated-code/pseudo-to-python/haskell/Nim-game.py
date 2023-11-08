import sys

prompt = "How many do you take? 1, 2 or 3? "

def getPlayerSelection():
    c = int(input(prompt))
    if c in [1, 2, 3]:
        return c
    else:
        print("Invalid input")
        return getPlayerSelection()

def play(n):
    print(str(n) + token(n) + " remain.")
    if n == 0:
        print("Computer Wins!")
    else:
        playerSelection = getPlayerSelection()
        if playerSelection > 4:
            computerSelection = playerSelection - 4
        else:
            computerSelection = 4 - playerSelection
        print("Computer takes " + str(computerSelection) + token(computerSelection) + ".\n")
        play(n - computerSelection - playerSelection)

def token(n):
    if n == 1:
        return " token"
    else:
        return " tokens"

play(12)