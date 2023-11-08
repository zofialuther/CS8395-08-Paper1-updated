from functools import reduce

def seriesSumA(f):
    '''The sum of the map of f over xs.'''
    return lambda xs: sum(map(f, xs))

def seriesSumB(f):
    '''Folding acc + f(x) over xs where acc begins at 0.'''
    return lambda xs: reduce(lambda a, x: a + f(x), xs, 0)

def main():
    '''Summing 1/x^2 over x = 1..1000'''
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
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))

def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))

def fTable(s):
    '''Heading -> x display function -> fx display function ->
          f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + (
                ' -> '
            ) + fxShow(f(x)) for x in xs
        ])
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )

if __name__ == '__main__':
    main()