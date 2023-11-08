```python
from functools import reduce
from operator import itemgetter

def consolidated(pairs):
    def go(xy, abetc):
        if not abetc:
            return [xy]
        x, y = xy
        (a, b), *etc = abetc
        if y >= b:
            return [xy, *etc]
        elif y >= a:
            return [(x, b), *etc]
        else:
            return [xy, *abetc]
    def ab(pair):
        a, b = pair
        return (a, b) if a <= b else (b, a)
    return reduce(go, sorted(map(ab, pairs), key=itemgetter(1), reverse=True), [])

tests = [ [], [(1.1, 2.2)], [(6.1, 7.2), (7.2, 8.3)], [(4, 3), (2, 1)], [(4, 3), (2, 1), (-1, -2), (3.9, 10)], [(1, 3), (-6, -1), (-4, -5), (8, 2), (-6, -6)] ]

def tabulated(s, xShow, fxShow, f, xs):
    w = len(max(map(xShow, xs), key=len))
    def rjust(n, c, s):
        return s.rjust(n, c)
    return '\n'.join([s] + [xShow(x).rjust(w) + " -> " + fxShow(f(x)) for x in xs])

def showPairs(xs):
    if not xs:
        return "[]"
    return '[' + ', '.join([showPair(x) for x in xs]) + ']'

def showPair(pair):
    a, b = pair
    return '(' + showNum(a) + ', ' + showNum(b) + ')'

def showNum(n):
    if n - int(n) == 0:
        return str(int(n))
    else:
        return str(n)

print(tabulated("Range consolidations:", showPairs, showPairs, consolidated, tests))
```