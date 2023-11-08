from operator import itemgetter
from itertools import accumulate, chain, islice

def bellNumbers():
    return list(map(itemgetter(0), bellTriangle()))

def bellTriangle():
    return list(map(
        itemgetter(1),
        iterate(
            compose(
                bimap(last)(identity),
                list, uncurry(scanl(lambda x, y: x + y))
            )
        )((1, [1]))
    ))

def main():
    showIndex = compose(repr, succ, itemgetter(0))
    showValue = compose(repr, itemgetter(1))
    print(
        fTable(
            'First fifteen Bell numbers:'
        )(showIndex)(showValue)(identity)(list(
            enumerate(take(15)(bellNumbers()))
        ))
    )

    print('\nFiftieth Bell number:')
    bells = bellNumbers()
    drop(49)(bells)
    print(
        next(bells)
    )

    print(
        fTable(
            "\nFirst 10 rows of Bell's triangle:"
        )(showIndex)(showValue)(identity)(list(
            enumerate(take(10)(bellTriangle()))
        ))
    )

def bimap(f):
    return lambda g: lambda x: (f(x), g(x))

def compose(fs):
    return reduce(go, fs, identity)

def drop(n):
    return lambda xs: xs[n:] if isinstance(xs, (list, tuple, str)) else take(n)(xs)

def fTable(s):
    return lambda xShow: lambda fxShow: lambda f: lambda xs: s + '\n' + '\n'.join(
        map(arrowed, xs, map(xShow, xs))
    )
    def arrowed(x, y):
        return y.rjust(max(map(len, map(xShow, xs)), ' ') + ' -> ' + fxShow(f(x))

def identity(x):
    return x

def iterate(f):
    def gen(x):
        v = x
        while True:
            yield v
            v = f(v)
    return gen

def last(xs):
    return xs[-1]

def scanl(f):
    return lambda a: lambda xs: list(accumulate(chain([a], xs), f))

def succ(x):
    return 1 + x

def take(n):
    return lambda xs: xs[0:n] if isinstance(xs, (list, tuple)) else list(islice(xs, n))

def uncurry(f):
    return lambda tpl: f(tpl[0])(tpl[1])

if __name__ == '__main__':
    main()