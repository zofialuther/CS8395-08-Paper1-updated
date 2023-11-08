from optparse import OptionParser
import random

class Opts:
    def __init__(self, optLength, optCount, optReadable):
        self.optLength = optLength
        self.optCount = optCount
        self.optReadable = optReadable

parser = OptionParser()
parser.add_option("--length", dest="optLength", default=8, help="password length")
parser.add_option("--count", dest="optCount", default=1, help="number of passwords to be generated")
parser.add_option("--readable", action="store_true", dest="optReadable", default=False, help="Whether to use only readable characters")
(options, args) = parser.parse_args()

opts = Opts(int(options.optLength), int(options.optCount), options.optReadable)

charSets = [list(map(chr, range(97, 123))), list(map(chr, range(65, 91))), list(map(str, range(10))), list("!\"#$%&'()*+,-./:;<=>?@[]^_{|}~")]

visualySimilar = ["l", "IOSZ", "012", "!|.,"]

def password(charSets, length):
    password = ''
    for charSet in charSets:
        password += random.choice(charSet)
    return password

for _ in range(opts.optCount):
    s = charSets
    if opts.optReadable:
        s = [list(set(charSets[i]) - set(visualySimilar[i])) for i in range(4)]
    res = password(s, max(4, opts.optLength))
    print(res)