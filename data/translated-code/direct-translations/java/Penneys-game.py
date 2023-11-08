from random import randint

def main():
    compChoice = ""
    if randint(0, 1):
        for i in range(3):
            compChoice += "HT"[randint(0, 1)]
        print(f"Computer chooses {compChoice}")
        playerChoice = prompt(compChoice)
    else:
        playerChoice = prompt(compChoice)
        compChoice = "T" if playerChoice[1] == 'T' else "H"
        compChoice += playerChoice[:2]
        print(f"Computer chooses {compChoice}")
    
    tossed = ""
    while True:
        tossed += "HT"[randint(0, 1)]
        print(f"Tossed {tossed}")
        if tossed.endswith(playerChoice):
            print("You win!")
            break
        if tossed.endswith(compChoice):
            print("Computer wins!")
            break

def prompt(otherChoice):
    s = ""
    while True:
        s = input("Choose a sequence: ").strip().upper()
        if len(s) == 3 and all(c in "HT" for c in s) and s != otherChoice:
            break
    return s

if __name__ == "__main__":
    main()