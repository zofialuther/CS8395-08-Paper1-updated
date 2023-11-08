from itertools import accumulate, chain, count, islice
from operator import add, mul

def leftFact():
    return accumulate(chain([0], fact()), add)

def fact():
    return accumulate(chain([1], count(1)), mul)

def main():
    print('Terms 0 thru 10 inclusive:\n  %r' % take(11)(leftFact()))

    print('\nTerms 20 thru 110 (inclusive) by tens:')
    for x in takeFromThenTo(20)(30)(110)(leftFact()):
        print(x)

    print('\n\nDigit counts for terms 1k through 10k (inclusive) by k:\n  %r' % list(map(compose(len)(str), takeFromThenTo(1000)(2000)(10000)(leftFact()))))

def compose(g):
    return lambda f: lambda x: g(f(x))

def scanl(f):
    def go(a):
        def g(xs):
            return accumulate(chain([a], xs), f)
        return g
    return go

def take(n):
    return lambda xs: (xs[0:n] if isinstance(xs, list) else list(islice(xs, n)))

def takeFromThenTo(a):
    return lambda b: lambda z: lambda xs: islice(xs, a, 1 + z, b - a)

if __name__ == '__main__':
    main()