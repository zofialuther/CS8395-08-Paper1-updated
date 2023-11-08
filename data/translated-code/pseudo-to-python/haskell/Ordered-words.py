def isSorted(wws):
    return all(x <= y for x, y in zip(wws, wws[1:]))

def getLines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def main():
    ls = getLines("unixdict.txt")
    ow = list(filter(isSorted, ls))
    maxl = max(len(w) for w in ow)
    print([w for w in ow if len(w) == maxl])