```python
def chr(x):
    return chr(x)

def fromMaybe(x, y):
    if x is None:
        return y
    else:
        return x

def swap(x, y):
    return (y, x)

def getArgs():
    return sys.argv[1:]

class Command:
    def __init__(self, action, string):
        self.action = action
        self.string = string

alphabet = [chr(x) for x in range(32, 127)]
cipherMap = dict(zip(alphabet, shuffle(20, alphabet)))

def shuffle(n, xs):
    return iterate(go, xs)[n]

def go(xs):
    if not xs:
        return []
    else:
        return go(xs[2:]) + xs[:2]

def convert(m, xs):
    return [fromMaybe(x, m.get(x)) for x in xs]

def runCommand(command):
    if isinstance(command, Cipher):
        return convert(cipherMap, command.string)
    elif isinstance(command, Decipher):
        return convert(dict((swap(x) for x in cipherMap.items())), command.string)
    elif isinstance(command, Invalid):
        return "Invalid arguments. Usage: simplecipher c|d <text>"

def parseArgs(args):
    if len(args) >= 2:
        if args[0] == "c":
            return Cipher(args[1])
        elif args[0] == "d":
            return Decipher(args[1])
        else:
            return Invalid()
    else:
        return Invalid()

def main():
    args = getArgs()
    command = parseArgs(args)
    result = runCommand(command)
    print(result)
```