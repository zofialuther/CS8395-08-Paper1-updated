```python
from itertools import chain, count, islice
from math import gcd

def farey(n):
    def go(k):
        return chain.from_iterable(
            map(lambda m: [(m, k)], range(0, k+1))
        ) if k > 0 else [(0, 1)]
    return sorted(
        list(set(go(k) for k in range(0, n+1))),
        key=lambda f: f[0] / f[1]
    )

def fareyLength(n):
    def go(x):
        return (x * (x + 3)) // 2 - sum(
            go(x // k) for k in range(2, x+1)
        )
    return go(n)

def showFarey(xs):
    return '(' + ', '.join(map(lambda x: str(x[0]) + '/' + str(x[1]), xs)) + ')'

def main():
    print(
        fTable(
            'Farey sequence for orders 1-11 (inclusive):\n'
        )(str)(showFarey)(
            farey
        )(list(range(1, 12)))
    )
    print(
        fTable(
            '\n\nNumber of fractions in the Farey sequence ' +
            'for order 100 through 1,000 (inclusive) by hundreds:\n'
        )(str)(str)(
            fareyLength
        )(list(range(100, 1001, 100)))
    )

def bind(xs):
    return lambda f: list(
        chain.from_iterable(
            map(f, xs)
        )
    )

def compose(g):
    return lambda f: lambda x: g(f(x))

def enumFromThenTo(m):
    def go(nxt, n):
        d = nxt - m
        return islice(count(0), m, d + n, d)
    return lambda nxt: lambda n: (
        list(go(nxt, n))
    )

def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))

def eq(a):
    return lambda b: a == b

def fromRatio(r):
    return r[0] / r[1]

def nubBy(p):
    def go(xs):
        if not xs:
            return []
        x = xs[0]
        return [x] + go(
            list(filter(
                lambda y: not p(x)(y),
                xs[1:]
            ))
        )
    return lambda xs: go(xs)

def on(f):
    return lambda g: lambda a: lambda b: f(g(a))(g(b))

def ratio(n):
    def go(n, d):
        g = gcd(n, d)
        return (n // g, d // g)
    return lambda d: go(n * signum(d), abs(d))

def showRatio(r):
    d = r[1]
    return str(r[0]) + (
        '/' + str(d) if 1 != d else ''
    )

def signum(n):
    return -1 if 0 > n else (1 if 0 < n else 0)

def fTable(s):
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )

def unlines(xs):
    return '\n'.join(xs)

if __name__ == '__main__':
    main()
```