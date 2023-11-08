def runGame(tokens):
    print("Nim game.")
    while tokens > 0:
        humanInputOk = False
        humanTokens = 0
        while not humanInputOk:
            try:
                humanTokens = int(input("Human takes how many tokens?  "))
                if 1 <= humanTokens <= 3:
                    humanInputOk = True
                else:
                    print("Try a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Try a number between 1 and 3.")
        tokens -= humanTokens
        print("You take " + str(humanTokens) + " token(s). " + str(tokens) + " token(s) remaining.")
        if tokens == 0:
            print("You win!!.")
            break
        computerTokens = 4 - humanTokens
        tokens -= computerTokens
        print("Computer takes " + str(computerTokens) + " token(s). " + str(tokens) + " token(s) remaining.")
        if tokens == 0:
            print("Computer wins!!.")
            break

runGame(12)