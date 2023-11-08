from functools import reduce

def isSorted(wws):
    return all(x <= y for x, y in zip(wws, wws[1:]))

def getLines(filename):
    with open(filename, 'r') as file:
        return file.readlines()

if __name__ == "__main__":
    ls = getLines("unixdict.txt")
    ow = list(filter(isSorted, ls))
    maxl = reduce(lambda x, y: x if len(x) > len(y) else y, ow)
    print(list(filter(lambda w: len(w) == len(maxl), ow)))