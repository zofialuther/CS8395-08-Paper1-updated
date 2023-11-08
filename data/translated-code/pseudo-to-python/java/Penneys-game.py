import random

def main():
    rand = random.Random()
    compChoice = ""
    playerChoice = input("Enter your choice (HT): ")
    if rand.choice([True, False]):
        compChoice = rand.choice("HT")
        print("Computer chooses", compChoice)
        playerChoice = input("Enter your choice (HT): ")
    else:
        playerChoice = input("Enter your choice (HT): ")
        compChoice = "T"
        if playerChoice[1] == 'T':
            compChoice = "H"
        compChoice += playerChoice[:2]
        print("Computer chooses", compChoice)

    tossed = ""
    while True:
        tossed += rand.choice("HT")
        print("Tossed", tossed)
        if tossed.endswith(playerChoice):
            print("You win!")
            break
        if tossed.endswith(compChoice):
            print("Computer wins!")
            break

def prompt(otherChoice):
    s = ""
    while True:
        s = input("Choose a sequence (HT): ").strip().upper()
        if len(s) == 2 and all(char in "HT" for char in s) and s != otherChoice:
            return s

main()