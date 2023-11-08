def isVowel(c):
    if c.upper() == 'A' or c.upper() == 'E' or c.upper() == 'I' or c.upper() == 'O' or c.upper() == 'U':
        return True
    else:
        return False

def isSpecial(c):
    if c.upper() == 'B' or c.upper() == 'F' or c.upper() == 'M':
        return True
    else:
        return False

def shorten(name):
    if isVowel(name[0]):
        return ''.join(map(str.lower, name))
    else:
        return ''.join(map(str.lower, name[1:]))

def line(prefix, letter, name):
    if name[0].lower() == letter.lower():
        return prefix + shorten(name) + "\n"
    else:
        return prefix + letter.lower() + shorten(name) + "\n"

def theNameGame(name):
    return line(name + ", " + name + ", bo-", 'b', name) + line("Banana-fana fo-", 'f', name) + line("Fee-fi-mo-", 'm', name) + name + "!\n"

def main():
    names = ["Gary", "Earl", "Billy", "Felix", "Mike", "Steve"]
    for name in names:
        print(theNameGame(name))

main()