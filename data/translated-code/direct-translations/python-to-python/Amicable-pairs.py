from itertools import chain
from math import sqrt

def amicablePairsUpTo(n):
    sigma = compose(sum)(properDivisors)

    def amicable(x):
        y = sigma(x)
        return [(x, y)] if (x < y and x == sigma(y)) else []

    return concatMap(amicable)(
        enumFromTo(1)(n)
    )

def main():
    for x in amicablePairsUpTo(20000):
        print(x)

def compose(g):
    return lambda f: lambda x: g(f(x))

def concatMap(f):
    return lambda xs: (''.join if isinstance(xs, str) else list)(
        chain.from_iterable(map(f, xs))
    )

def enumFromTo(m):
    def go(n):
        return list(range(m, 1 + n))
    return lambda n: go(n)

def properDivisors(n):
    root_ = sqrt(n)
    intRoot = int(root_)
    blnSqr = root_ == intRoot
    lows = [x for x in range(1, 1 + intRoot) if 0 == n % x]
    return lows + [
        n // x for x in reversed(
            lows[1:-1] if blnSqr else lows[1:]
        )
    ]

if __name__ == '__main__':
    main()