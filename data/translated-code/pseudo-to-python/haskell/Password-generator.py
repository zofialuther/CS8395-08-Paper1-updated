from optparse import OptionParser
import random
import string

class Opts:
    def __init__(self):
        self.optLength = 8
        self.optCount = 1
        self.optReadable = False

def defineOptions(parser):
    parser.add_option("-l", "--length", dest="optLength", type="int", default=8, help="password length")
    parser.add_option("-c", "--count", dest="optCount", type="int", default=1, help="number of passwords to be generated")
    parser.add_option("-r", "--readable", action="store_true", dest="optReadable", default=False, help="Whether to use only readable characters")

def password(s, l):
    return ''.join(random.choice(s) for _ in range(l))

def main():
    parser = OptionParser()
    defineOptions(parser)
    (options, args) = parser.parse_args()

    n = options.optCount
    l = options.optLength
    if options.optReadable:
        charSets = [set(string.ascii_lowercase), set(string.ascii_uppercase), set(string.digits), set("!\"#$%&'()*+,-./:;<=>?@[]^_{|}~")]
        visualySimilar = [set(["l"]), set(["I","O","S","Z"]), set(["0","1","2"]), set(["!","|","."])]
        s = [c for c in map(''.join, zip(*[sorted(s) for s in charSets]))]
        s = [s - set(''.join(visualySimilar[i])) for i, s in enumerate(s)]
    else:
        charSets = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "!\"#$%&'()*+,-./:;<=>?@[]^_{|}~"]
        s = charSets

    res = [password(s[i], max(4, l)) for i in range(n)]
    for r in res:
        print(r)

if __name__ == "__main__":
    main()