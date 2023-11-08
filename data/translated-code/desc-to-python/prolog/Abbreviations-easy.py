command_table = {
    "run": ["execute", "start", "launch"],
    "stop": ["end", "terminate", "finish"],
    "pause": ["suspend", "hold", "freeze"]
}

def validate(word):
    for command in command_table:
        if word.lower() in [c.lower() for c in [command] + command_table[command]]:
            return command
    return None

def main(args):
    validated_commands = [validate(arg) for arg in args]
    for command in validated_commands:
        if command:
            print(command)
        else:
            print("Invalid command")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])