```python
from itertools import accumulate, chain, takewhile, dropwhile, product, islice
from functools import reduce
from string import digits, ascii_lowercase

def estheticNumbersInBase(b):
    def fromBaseDigits(b):
        def go(digitList):
            maybeNum = reduce(lambda r, d: None if r is None or (0 > d or d >= b) else r * b + d, digitList, 0)
            return [] if maybeNum is None else [maybeNum]
        return go

    def compose(*fs):
        def go(f, g):
            def fg(x):
                return f(g(x))
            return fg
        return reduce(go, fs, lambda x: x)

    def concatMap(f):
        def go(xs):
            return chain.from_iterable(map(f, xs))
        return go

    def scanl(f):
        def go(a):
            def g(xs):
                return accumulate(chain([a], xs), f)
            return g
        return go

    def take(n):
        def go(xs):
            return list(islice(xs, n))
        return go

    def takeWhile(p):
        return lambda xs: list(takewhile(p, xs))

    def dropWhile(p):
        return lambda xs: list(dropwhile(p, xs))

    def replicateList(xs):
        def rep(n):
            def go(x):
                return [[]] if x < 1 else [([a] + b) for (a, b) in product(xs, go(x - 1))]
            return go(n)
        return rep

    deltas = concatMap(
        compose(
            lambda deltas: 
                concatMap(
                    lambda headDigit: 
                        concatMap(
                            compose(fromBaseDigits(b), scanl(lambda x, y: x + y))
                        )(deltas)
                )(range(1, b))
        ),
        replicateList([-1, 1])
    )(count(0))
    return deltas

def samples(b):
    def showInBase(b):
        charSet = digits + ascii_lowercase
        def toBaseDigits(b):
            def f(x):
                return None if x == 0 else divmod(x, b)[::-1]
            return lambda n: list(reversed(unfoldr(f)(n)))
        return lambda n: ''.join(charSet[i] for i in toBaseDigits(b)(n))

    i, j = b * 4, b * 6
    return 'Esthetics [' + str(i) + '..' + str(j) + '] for base ' + str(b) + ':' + unlines(wrap(unwords(showInBase(b)(n) for n in compose(drop(i - 1), take(j))(estheticNumbersInBase(b))), 60))

def takeInRange(a, b):
    def takeInRangeHelper(x):
        return list(takewhile(lambda x: x <= b, dropwhile(lambda x: x < a, x)))
    return takeInRangeHelper

def main():
    for b in range(2, 17):
        print(samples(b))
    for (lo, hi) in [(1000, 9999), (100_000_000, 130_000_000)]:
        print("Base 10 Esthetics in range [{lo}..{hi}]:")
        print(unlines(wrap(unwords(str(x) for x in takeInRange(lo, hi)(estheticNumbersInBase(10)), 60)))

if __name__ == '__main__':
    main()
```