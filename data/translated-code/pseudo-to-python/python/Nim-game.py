print("Py Nim\n")

def getTokens(curTokens):
    global tokens
    
    take = int(input("How many tokens would you like to take? "))
    
    if take < 1 or take > 3:
        print("Number must be between 1 and 3.\n")
        getTokens(curTokens)
        return
    
    tokens = curTokens - take
    print("You take " + str(take) + " tokens.")
    print(str(tokens) + " tokens remaining.\n")

def compTurn(curTokens):
    global tokens
    
    take = curTokens % 4
    tokens = curTokens - take
    print("Computer takes " + str(take) + " tokens.")
    print(str(tokens) + " tokens remaining.\n")

tokens = 12
while tokens > 0:
    getTokens(tokens)
    compTurn(tokens)

print("Computer wins!")