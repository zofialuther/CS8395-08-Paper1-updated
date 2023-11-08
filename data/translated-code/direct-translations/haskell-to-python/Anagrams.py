from itertools import groupby
from operator import itemgetter

def groupon(f, x, y):
    return f(x) == f(y)

def main():
    with open("./../Puzzels/Rosetta/unixdict.txt", "r") as file:
        words = file.readlines()
        words = [word.strip() for word in words]
        wix = [list(group) for key, group in groupby(sorted(zip(map(sorted, words), words), key=lambda x: x[0]), key=lambda x: groupon(itemgetter(0), x[0][0], x[1][0]))]
        mxl = max(len(group) for group in wix)
        for group in wix:
            if len(group) == mxl:
                print([word[1] for word in group])

main()