from itertools import accumulate, chain, count, islice
from fractions import Fraction

def faulhaberTriangle(m):
    def go(rs, n):
        def f(x, y):
            return Fraction(n, x) * y
        xs = map(f, islice(count(2), m), rs)
        return [Fraction(1 - sum(xs), 1)] + list(xs)
    
    return list(accumulate([[]] + list(islice(count(0), 1 + m)), go))[1:]

def faulhaberSum(p, n):
    def go(x, y):
        return y * (n ** x)

    return sum(map(go, count(1), faulhaberTriangle(p)[-1]))

def main():
    fs = faulhaberTriangle(9)
    print(fTable(__doc__ + ':\n')(str)(compose(concat))(fmap(showRatio(3)(3)))(index(fs))(range(0, len(fs)))
    print('')
    print(faulhaberSum(17, 1000))

def fTable(s):
    def gox(xShow):
        def gofx(fxShow):
            def gof(f):
                def goxs(xs):
                    ys = list(map(xShow, xs))
                    w = max(map(len, ys))

                    def arrowed(x, y):
                        return y.rjust(w, ' ') + ' -> ' + (fxShow(f(x)))
                    return s + '\n' + '\n'.join(map(arrowed, xs, ys))
                return goxs
            return gof
        return gofx
    return gox

def compose(g):
    return lambda f: lambda x: g(f(x))

def concat(xs):
    def f(ys):
        zs = list(chain(*ys))
        return ''.join(zs) if isinstance(ys[0], str) else zs
    return f(xs) if isinstance(xs, list) else (chain.from_iterable(xs)) if xs else []

def fmap(f):
    def go(xs):
        return list(map(f, xs))
    return go

def index(xs):
    return lambda n: None if 0 > n else (xs[n] if (hasattr(xs, "__getitem__")) else next(islice(xs, n, None))

def showRatio(m):
    def go(n):
        def f(r):
            d = r.denominator
            return str(r.numerator).rjust(m, ' ') + (('/' + str(d).ljust(n, ' ')) if 1 != d else (' ' * (1 + n)))
        return f
    return go

if __name__ == '__main__':
    main()