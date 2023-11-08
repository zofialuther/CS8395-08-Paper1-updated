```python
def isAbbreviationOf(abbreviation, command):
    return abbreviation.lower() in command.lower()

def expandAbbreviation(abbreviation, command_table):
    for command in command_table:
        if isAbbreviationOf(abbreviation, command):
            return command
    return None

def main():
    command_table = ["move", "attack", "defend", "wait"]
    user_input = input("Enter your command: ")
    commands = user_input.split()
    expanded_commands = [expandAbbreviation(command, command_table) or command for command in commands]
    print("Expanded commands:", " ".join(expanded_commands))

main()
```