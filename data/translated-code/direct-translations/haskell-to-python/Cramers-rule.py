```python
from fractions import Fraction

def s_permutations(arr):
    def aux(items, x):
        result = []
        for f, item in zip(cycle([reverse, lambda x: x]), items):
            result.append(f(insertEv(x, item)))
        return result

    def insertEv(x, l):
        if len(l) == 0:
            return [[x]]
        else:
            return [[x] + l] + list(map(lambda y: [l[0]] + y, insertEv(x, l[1:])))

    result = list(zip(cycle([1, -1]), foldl(aux, [[]], arr)))
    return result

def mult(uss, vss):
    return list(map(lambda xs: [] if len(xs) == 0 else functools.reduce(lambda a, b: list(map(lambda x, y: x + y, a, b)), xs), list(map(lambda vs, u: list(map(lambda x, y: u * x, vs)), vss, uss))))

def matI(n):
    return [[Fraction(1 if i == j else 0) for i in range(n)] for j in range(n)]

def elemPos(ms, i, j):
    return ms[i][j]

def prod(f, ms, i):
    return functools.reduce(lambda a, b: a * f(ms, i, b), range(len(ms[0])), 1)

def s_determinant(f, ms, arr):
    return sum([f(ms, i, s) * s for i, s in arr])

def elemCramerPos(l, k, ks, ms, i, j):
    return elemPos(ms, i, j) if j != l else elemPos(ks, i, k)

def solveCramer(ms, ks):
    d = s_determinant(elemPos, ms, s_permutations(range(len(ms))))
    ls = range(len(ms))
    ps = s_permutations(ls)
    if d != 0:
        result = []
        for u in reversed(ls):
            us = list(map(lambda l: s_determinant(lambda i, j: elemCramerPos(l, u, ks, ms, i, j), ms, ps), ls))
            result = [list(map(lambda y, ys: [y] + ys, us, result))]
        return result
    else:
        return []

def task(a, b):
    x = solveCramer(a, b)
    u = list(map(lambda l: list(map(float, l)), x))
    y = mult(a, x)
    identity = matI(len(x))
    a1 = solveCramer(a, identity)
    h = mult(a, a1)
    z = mult(a1, b)
    print("a =")
    print(a)
    print("b =")
    print(b)
    print("solve: a * x = b => x = solveCramer a b =")
    print(x)
    print("u = fromRationaltoDouble x =")
    print(u)
    print("verification: y = a * x = mult a x =")
    print(y)
    print("test: y == b = ")
    print(y == b)
    print("identity matrix: identity =")
    print(identity)
    print("find: a1 = inv(a) => solve: a * a1 = identity => a1 = solveCramer a identity =")
    print(a1)
    print("verification: h = a * a1 = mult a a1 =")
    print(h)
    print("test: h == identity = ")
    print(h == identity)
    print("z = a1 * b = mult a1 b =")
    print(z)
    print("test: z == x =")
    print(z == x)

a  = [[2, -1, 5, 1],
      [3, 2, 2, -6],
      [1, 3, 3, -1],
      [5, -2, -3, 3]]
b = [[-3], [-32], [-47], [49]]
task(a, b)
```