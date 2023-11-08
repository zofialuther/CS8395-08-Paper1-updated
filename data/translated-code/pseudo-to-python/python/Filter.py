```python
from itertools import chain
import re
import inspect

def f1(xs):
    return reduce(lambda a, x: a + [x] if even(x) else a, xs, [])

def f2(xs):
    return concatMap(lambda x: [x] if even(x) else [])(xs)

def f3(xs):
    return (x for x in xs if even(x))

def f4(xs):
    return list(filter(even, xs))

def main():
    xs = enumFromTo(0)(10)
    print(tabulated(showReturn)('By descending generality and increasing brevity:\n')(lambda f: list(f(xs)))([f1, f2, f3, f4]))

def concatMap(f):
    return lambda xs: list(chain.from_iterable(map(f, xs)))

def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))

def even(x):
    return 0 == x % 2

def showReturn(f):
    return re.split('return ', inspect.getsource(f))[-1].strip()

def tabulated(fShow):
    def go(s, f, xs):
        w = max(len(fShow(x)) for x in xs)
        return s + '\n' + '\n'.join([fShow(x).rjust(w, ' ') + ' -> ' + str(f(x)) for x in xs])
    return lambda s: lambda f: lambda xs: go(s, f, xs)

if __name__ == '__main__':
    main()
```