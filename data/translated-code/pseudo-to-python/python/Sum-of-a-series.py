def seriesSumA(f):
    return lambda xs: sum(map(f, xs))


def seriesSumB(f):
    return lambda xs: reduce(
        lambda a, x: a + f(x), xs, 0
    )


def main():
    def f(x):
        return 1 / (x * x)

    print(
        fTable(
            __doc__ + ':\n' + '(1/x^2 over x = 1..1000)'
        )(lambda f: '\tby ' + f.__name__)(str)(
            lambda g: g(f)(enumFromTo(1)(1000))
        )([seriesSumA, seriesSumB])
    )


def compose(g):
    return lambda f: lambda x: g(f(x))


def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))


def fTable(s):
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )


if __name__ == '__main__':
    main()