import itertools
from os.path import *

def abbrevLen(xs):
    n = len(xs)
    return len(os.path.commonprefix(xs))

def main():
    with open('weekDayNames.txt', 'r') as file:
        xs = file.readlines()
        for s in xs:
            print(abbrevLen(s), s)

def compose(g):
    return lambda f: lambda x: g(f(x))

def concat(xs):
    return ''.join(xs)

def inits(xs):
    return [xs[:i] for i in range(len(xs)+1)]

def lines(s):
    return s.split('\n')

map_ = lambda f: lambda xs: list(map(f, xs))

def nub(xs):
    return list(dict.fromkeys(xs))

def readFile(fp):
    with open(fp, 'r') as file:
        return file.read()

def scanl(f):
    return lambda xs: list(itertools.accumulate(xs, f))

def strip(s):
    return s.strip()

def transpose(m):
    return list(zip(*m))

def words(s):
    return s.split()

if __name__ == "__main__":
    main()