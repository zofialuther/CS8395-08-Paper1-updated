```python
import Data.Map.Strict as Map
import Data.Set as Set
from Data.Monoid import (<>)

def triangles(f, n):
    mapRoots = Map.fromList([(x, x**2) for x in range(1, n+1)])
    triSet = Set()
    for a in range(1, n+1):
        for b in range(1, a):
            suma2b2 = (a * a) + (b * b)
            result = f(mapRoots, suma2b2, (a * b), a, b)
            if result is not None:
                triSet.add((a, b, result))
    return triSet

def f90(dct, x2, ab, a, b):
    return dct.get(x2)

def f60(dct, x2, ab, a, b):
    return dct.get(x2 - ab)

def f120(dct, x2, ab, a, b):
    return dct.get(x2 + ab)

def f60ne(dct, x2, ab, a, b):
    if a == b:
        return None
    else:
        return dct.get(x2 - ab)

print("Triangles of maximum side 13")
solns = triangles(f120, 13)
for f, n in zip([f120, f90, f60], [120, 90, 60]):
    print(str(len(solns)) + " solutions for " + str(n) + " degrees:")
    for soln in solns:
        print(soln)

print("60 degrees - uneven triangles of maximum side 10000. Total:")
print(len(triangles(f60ne, 10000)))
```