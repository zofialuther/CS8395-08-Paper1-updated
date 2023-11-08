```python
from functools import reduce

def s_permutations(arr):
    def aux(items, x):
        result = []
        for f, item in zip(cycle([reverse, id]), items):
            result.extend(f(insertEv(x, item)))
        return result
    
    def insertEv(x, l):
        if len(l) == 0:
            return [[x]]
        else:
            return [[x] + l] + list(map(lambda y: [l[0]] + y, insertEv(x, l[1:])))
    
    result = []
    for i in range(1, len(arr) + 1):
        result.append((arr, i))
    return result

def mult(uss, vss):
    def multHelper(vs, u):
        return list(map(lambda x: u * x, vs))
    
    def sumList(xs):
        if len(xs) == 0:
            return []
        else:
            return list(reduce(lambda a, b: list(map(lambda x, y: x + y, a, b)), xs))
    
    return list(map(lambda xs: sumList(list(map(lambda vs: multHelper(vs, xs[i]), vss))), uss))

def matI(n):
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]

def elemPos(ms, i, j):
    return ms[i][j]

def prod(f, ms, i):
    result = 1
    for j in range(len(i)):
        result *= f(ms, i[j], j)
    return result

def s_determinant(f, ms, permutations):
    result = 0
    for is_, s in permutations:
        result += s * prod(f, ms, is_)
    return result

def elemCramerPos(l, k, ks, ms, i, j):
    if j != l:
        return elemPos(ms, i, j)
    else:
        return elemPos(ks, i, k)

def solveCramer(ms, ks):
    ls = list(range(len(ms)))
    ps = s_permutations(ls)
    d = s_determinant(elemPos, ms, ps)
    if d != 0:
        us = [col(u, ks, ms) for u in reversed(range(len(ks)))]
        return us
    else:
        return []

def task(a, b):
    x = solveCramer(a, b)
    u = list(map(lambda xs: list(map(float, xs)), x))
    y = mult(a, x)
    identity = matI(len(x))
    a1 = solveCramer(a, identity)
    h = mult(a, a1)
    z = mult(a1, b)
    print("a =")
    for row in a:
        print(row)
    print("b =")
    for row in b:
        print(row)
    print("solve: a * x = b => x = solveCramer a b =")
    for row in x:
        print(row)
    print("u = fromRationaltoDouble x =")
    for row in u:
        print(row)
    print("verification: y = a * x = mult a x =")
    for row in y:
        print(row)
    print("test: y == b = ")
    print(y == b)
    print("identity matrix: identity =")
    for row in identity:
        print(row)
    print("find: a1 = inv(a) => solve: a * a1 = identity => a1 = solveCramer a identity =")
    for row in a1:
        print(row)
    print("verification: h = a * a1 = mult a a1 =")
    for row in h:
        print(row)
    print("test: h == identity = ")
    print(h == identity)
    print("z = a1 * b = mult a1 b =")
    for row in z:
        print(row)
    print("test: z == x =")
    print(z == x)

a = [[2,-1, 5, 1], [3, 2, 2,-6], [1, 3, 3,-1], [5,-2,-3, 3]]
b = [[-3], [-32], [-47], [49]]
task(a, b)
```