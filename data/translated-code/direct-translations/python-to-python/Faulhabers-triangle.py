```python
from itertools import accumulate, chain, count, islice
from fractions import Fraction

def faulhaberTriangle(m):
    def go(rs, n):
        def f(x, y):
            return Fraction(n, x) * y
        xs = list(map(f, islice(count(2), m), rs))
        return [Fraction(1 - sum(xs), 1)] + xs

    return list(accumulate(
        [[]] + list(islice(count(0), 1 + m)),
        go
    ))[1:]

def faulhaberSum(p, n):
    def go(x, y):
        return y * (n ** x)

    return sum(
        map(go, count(1), faulhaberTriangle(p)[-1])
    )

def main():
    fs = faulhaberTriangle(9)
    for row in fs:
        print([str(f) for f in row])

    print('')
    print(faulhaberSum(17, 1000))

if __name__ == '__main__':
    main()
```