```python
from itertools import chain, count, islice

def farey(n):
    def ratio(n, d):
        g = gcd(n, d)
        return {'type': 'Ratio', 'numerator': n // g, 'denominator': d // g}

    def fromRatio(r):
        return r.get('numerator') / r.get('denominator')

    def eq(a):
        return lambda b: a == b

    def on(f):
        return lambda g: lambda a: lambda b: f(g(a))(g(b))

    def nubBy(p):
        def go(xs):
            if not xs:
                return []
            x = xs[0]
            return [x] + go(list(filter(lambda y: not p(x)(y), xs[1:]))
        return lambda xs: go(xs)

    def bind(xs):
        return lambda f: list(chain.from_iterable(map(f, xs)))

    return sorted(nubBy(on(eq)(fromRatio))(bind(enumFromTo(1)(n))(lambda k: bind(enumFromTo(0)(k))(lambda m: ratio(m, k)))), key=fromRatio) + [ratio(1)(1)]

def fareyLength(n):
    def go(x):
        return (x * (x + 3)) // 2 - sum(go(x // k) for k in enumFromTo(2)(x))
    return go(n)

def showFarey(xs):
    return '(' + ', '.join(map(showRatio, xs)) + ')'

def main():
    print(fTable('Farey sequence for orders 1-11 (inclusive):\n')(str)(showFarey)(farey)(enumFromTo(1)(11)))
    print(fTable('\n\nNumber of fractions in the Farey sequence' + ' for order 100 through 1,000 (inclusive) by hundreds:\n')(str)(str)(fareyLength)(enumFromThenTo(100)(200)(1000)))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fTable(s):
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join((y.rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x, y in zip(xs, ys)))

    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(xShow, fxShow, f, xs)

def enumFromTo(m):
    return lambda n: list(range(m, n + 1))

def enumFromThenTo(m):
    def go(nxt, n):
        d = nxt - m
        return list(islice(count(0), m, d + n, d))
    return lambda nxt: lambda n: go(nxt, n)

def signum(n):
    return -1 if n < 0 else (1 if n > 0 else 0)

def unlines(xs):
    return '\n'.join(xs)

if __name__ == 'main':
    main()
```