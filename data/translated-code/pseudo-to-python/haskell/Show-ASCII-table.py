from Data.Char import *
from Data.List import *
from Data.List.Split import *
from Text.Printf import *

def asciiEntry(n):
    if n == 0:
        return n
    else:
        return "%d: %s" % (n, asciiName(n))

def asciiName(n):
    if n < 32:
        return []
    elif n > 127:
        return []
    elif n == 32:
        return "Spc"
    elif n == 127:
        return "Del"
    else:
        return chr(n)

def asciiTable():
    for chunk in chunks(16, range(32, 128)):
        for n in chunk:
            print(asciiEntry(n), end=" ")
        print("\n")

def main():
    asciiTable()