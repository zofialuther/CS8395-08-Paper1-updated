```python
import math
import random

def vecLeng(points):
    return math.sqrt((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2)

def findClosestPair(points):
    return foldl1''(lambda x, y: min(x, y, key=vecLeng), [[x, y] for x in points for y in points if x != y])

def testCP():
    g = random.Random()
    g.seed()
    pts = [g.uniform(-1, 1), g.uniform(-1, 1) for _ in range(1000)]
    print((findClosestPair(pts), vecLeng(findClosestPair(pts))))

def main():
    testCP()

def foldl1''(func, lst):
    return functools.reduce(func, lst)

```