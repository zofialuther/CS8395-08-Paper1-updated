```python
from functools import reduce
from itertools import count, islice

def scanl(f, base, l):
    yield base
    for x in l:
        base = f(base, x)
        yield base

def expand(p):
    return list(islice(scanl(lambda x, _: [1, *map(sum, zip(x, x[1:]))], [1], range(p)), p+1))

def test(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

def printPoly(p):
    return ' + '.join(f"{c}x^{i}" for i, c in enumerate(p) if c) or '0'

def main():
    for p in range(11):
        print(f"(x-1)^{p} expansion: {printPoly(expand(p))}")
    
    print("\nPrimes up to 100:")
    for i in range(101):
        if test(i):
            print(i, end=' ')

main()
```