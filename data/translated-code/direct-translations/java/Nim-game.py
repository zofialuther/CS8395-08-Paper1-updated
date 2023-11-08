```python
def runGame(tokens):
    print("Nim game.\n")
    
    while tokens > 0:
        humanInputOk = False
        humanTokens = 0
        while not humanInputOk:
            input_val = input("Human takes how many tokens? ")
            try:
                humanTokens = int(input_val)
                if 1 <= humanTokens <= 3:
                    humanInputOk = True
                else:
                    print("Try a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Try a number between 1 and 3.")
                
        tokens -= humanTokens
        print(f"You take {humanTokens} token{'s' if humanTokens > 1 else ''}. {tokens} token{'s' if tokens != 1 else ''} remaining.\n")
        
        if tokens == 0:
            print("You win!!\n")
            break
        
        computerTokens = 4 - humanTokens
        tokens -= computerTokens
        print(f"Computer takes {computerTokens} token{'s' if computerTokens != 1 else ''}. {tokens} token{'s' if tokens != 1 else ''} remaining.\n")
        
        if tokens == 0:
            print("Computer wins!!\n")
            break

runGame(12)
```