def main():
    print("Upper case: ")
    limit = 0
    for n in range(0, 0x10FFFF):
        if isUpperCase(n) and limit < 72:
            print(chr(n))
    print("...")

    print("Lower case: ")
    for n in range(0, 0x10FFFF):
        if isLowerCase(n) and limit < 72:
            print(chr(n))
    print("...")

def isUpperCase(character):
    return character.isupper()

def isLowerCase(character):
    return character.islower()