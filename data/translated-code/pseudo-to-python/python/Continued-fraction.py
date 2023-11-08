from fractions import Fraction
import itertools

def zip(a, b, t):
    return list(itertools.islice(itertools.izip(a, b), t))

def CF(a, b, t):
    terms = list(itertools.islice(zip(a, b, itertools.repeat(t))))
    z = Fraction(1, 1)
    for term in reversed(terms):
        z = term[0] + term[1] / z
    return z

def pRes(x, d):
    q, x = divmod(x, 1)
    res = str(q) + '.'
    for i in range(d):
        x *= 10
        q, x = divmod(x, 1)
        res += str(int(q))
    return res

def sqrt2_a():
    while True:
        yield 1
        yield 2

def sqrt2_b():
    while True:
        yield 1

cf = CF(sqrt2_a(), sqrt2_b(), 200)
print(pRes(cf, 200))

def Napier_a():
    n = 1
    while True:
        yield 2
        yield n
        n += 1

def Napier_b():
    while True:
        yield 1

cf = CF(Napier_a(), Napier_b(), 200)
print(pRes(cf, 200))

def Pi_a():
    while True:
        yield 3
        yield 6

def Pi_b():
    n = 1
    while True:
        yield 1
        n += 2
        yield n * n

cf = CF(Pi_a(), Pi_b(), 10)
print(pRes(cf, 10))