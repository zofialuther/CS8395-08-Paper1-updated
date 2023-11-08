from Data.Char import toLower
from Data.List import (\\)

def pangram(s):
    s = map(toLower, s)
    return null(s \\ ['a'..'z'])

def main():
    test_string = "How razorback-jumping frogs can level six piqued gymnasts!"
    print(pangram(test_string))