def isDigit(char):
    return char.isdigit()

def isOctDigit(char):
    return char.isdigit() and int(char) < 8

def isHexDigit(char):
    return char.isdigit() or char.upper() in ['A', 'B', 'C', 'D', 'E', 'F']

def areDigits(input_string):
    for char in input_string:
        if not isDigit(char):
            return False
    return True