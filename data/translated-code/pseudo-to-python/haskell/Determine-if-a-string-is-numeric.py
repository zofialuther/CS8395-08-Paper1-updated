def allDigits(str):
    for char in str:
        if not char.isdigit():
            return False
    return True

def isDigit(char):
    if '0' <= char <= '9':
        return True
    else:
        return False

def isOctDigit(char):
    if '0' <= char <= '7':
        return True
    else:
        return False

def isHexDigit(char):
    if '0' <= char <= '9' or 'A' <= char <= 'F' or 'a' <= char <= 'f':
        return True
    else:
        return False