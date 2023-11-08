from functools import reduce
from operator import mul

def fac(n):
    return reduce(mul, range(1, n+1))

def binCoef(n, k):
    return fac(n) // (fac(k) * fac(n - k))

pascal = lambda n: list(map(lambda k: binCoef(n, k), range(n+1)))