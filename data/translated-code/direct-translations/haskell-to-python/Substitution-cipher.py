```python
import string
import sys

alphabet = string.printable
cipherMap = list(zip(alphabet, alphabet[2:] + alphabet[:2]))

def shuffle(n, xs):
    return xs[n:] + xs[:n]

def convert(m, xs):
    return [m.get(x, x) for x in xs]

def runCommand(command, s):
    if command == "c":
        return ''.join(convert(dict(cipherMap), s))
    elif command == "d":
        return ''.join(convert(dict((b, a) for (a, b) in cipherMap), s))
    else:
        return "Invalid arguments. Usage: simplecipher c|d <text>"

def parseArgs(args):
    if len(args) >= 3:
        return (args[1], args[2])
    else:
        return ("", "")

if __name__ == "__main__":
    command, text = parseArgs(sys.argv)
    print(runCommand(command, text))
```