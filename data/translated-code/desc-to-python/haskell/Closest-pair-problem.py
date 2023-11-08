```python
import math
import random

def vecLeng(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def findClosestPair(points):
    def distance(p1, p2):
        return vecLeng(p1, p2)

    def closestPair(p1, p2):
        return min(p1, p2, key=lambda x: distance(x[0], x[1]))

    return min([closestPair(p1, p2) for p1 in points for p2 in points if p1 != p2], key=distance)

def testCP(n):
    points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
    print("Closest pair of points:", findClosestPair(points))

def main():
    testCP(10)

if __name__ == "__main__":
    main()
```