```python
import timeit
import random
from operator import itemgetter

def bruteForceClosestPair(point):
    numPoints = len(point)
    if numPoints < 2:
        return float('inf'), (None, None)
    return min(((abs(point[i] - point[j]), (point[i], point[j]))
                for i in range(numPoints-1)
                for j in range(i+1,numPoints)),
               key=itemgetter(0))

def closestPair(point):
    xP = sorted(point, key=lambda p: p.real)
    yP = sorted(point, key=lambda p: p.imag)
    return _closestPair(xP, yP)

def _closestPair(xP, yP):
    numPoints = len(xP)
    if numPoints <= 3:
        return bruteForceClosestPair(xP)
    Pl = xP[:numPoints//2]
    Pr = xP[numPoints//2:]
    Yl = []
    Yr = []
    xDivider = Pl[-1].real
    for p in yP:
        if p.real <= xDivider:
            Yl.append(p)
        else:
            Yr.append(p)
    dl, pairl = _closestPair(Pl, Yl)
    dr, pairr = _closestPair(Pr, Yr)
    dm, pairm = (dl, pairl) if dl < dr else (dr, pairr)
    closeY = [p for p in yP if abs(p.real - xDivider) < dm]
    numCloseY = len(closeY)
    if numCloseY > 1:
        closestY = min(((abs(closeY[i] - closeY[j]), (closeY[i], closeY[j]))
                        for i in range(numCloseY-1)
                        for j in range(i+1, min(i+8, numCloseY))),
                       key=itemgetter(0))
        return (dm, pairm) if dm <= closestY[0] else closestY
    else:
        return dm, pairm

def times():
    functions = [bruteForceClosestPair, closestPair]
    for f in functions:
        print('Time for', f.__name__, timeit.Timer(
            '%s(pointList)' % f.__name__,
            'from __main__ import %s, pointList' % f.__name__).timeit(number=1))

pointList = [random.randint(0,1000)+1j*random.randint(0,1000) for i in range(2000)]

if __name__ == '__main__':
    pointList = [(5+9j), (9+3j), (2+0j), (8+4j), (7+4j), (9+10j), (1+9j), (8+2j), 10j, (9+6j)]
    print(pointList)
    print('  bruteForceClosestPair:', bruteForceClosestPair(pointList))
    print('            closestPair:', closestPair(pointList))
    for i in range(10):
        pointList = [random.randrange(11)+1j*random.randrange(11) for i in range(10)]
        print('\n', pointList)
        print(' bruteForceClosestPair:', bruteForceClosestPair(pointList))
        print('           closestPair:', closestPair(pointList))
    print('\n')
    times()
    times()
    times()
```