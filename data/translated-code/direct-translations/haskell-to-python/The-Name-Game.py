```python
def isVowel(c):
    char = c.upper()
    if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False

def isSpecial(c):
    char = c.upper()
    if char == 'B' or char == 'F' or char == 'M':
        return True
    else:
        return False

def shorten(name):
    if isVowel(name[0]):
        return name.lower()
    else:
        return name[1:].lower()

def line(prefix, letter, name):
    if letter.lower() == name[0]:
        return prefix + shorten(name) + "\n"
    else:
        return prefix + letter.lower() + shorten(name) + "\n"

def theNameGame(name):
    return (line(name + ", " + name + ", bo-", 'b', name) +
            line("Banana-fana fo-", 'f', name) +
            line("Fee-fi-mo-", 'm', name) +
            name + "!\n")

names = ["Gary", "Earl", "Billy", "Felix", "Mike", "Steve"]
for name in names:
    print(theNameGame(name))
```