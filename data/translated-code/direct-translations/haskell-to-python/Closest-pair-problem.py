from math import sqrt
import random

from functools import reduce

def vecLeng(pair):
    a, b = pair[0]
    p, q = pair[1]
    return sqrt((a - p) ** 2 + (b - q) ** 2)

def findClosestPair(points):
    return reduce(lambda x, y: min(x, y, key=vecLeng), [((x, y), (p, q)) for x, *xs in points for y, *ys in xs for p, *ps in xs for q, *qs in ps])

def testCP():
    g = random.Random()
    g.seed(1)
    pts = [[g.uniform(-1, 1), g.uniform(-1, 1)] for _ in range(1000)]
    print((findClosestPair(pts)))

def main():
    testCP()

if __name__ == "__main__":
    main()