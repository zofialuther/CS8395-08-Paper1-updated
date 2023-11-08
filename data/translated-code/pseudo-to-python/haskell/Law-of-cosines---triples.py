def triangles(f, n):
    mapRoots = createMapRoots(n)
    triSet = set()
    for a in range(1, n+1):
        for b in range(1, a+1):
            suma2b2 = calculateSuma2b2(a, b)
            c = f(mapRoots, suma2b2, a * b, a, b)
            if c is not None:
                triSet.add((a, b, c))
    return triSet

def createMapRoots(n):
    mapRoots = {}
    for i in range(1, n+1):
        mapRoots[i * i] = i
    return mapRoots

def calculateSuma2b2(a, b):
    return a * a + b * b