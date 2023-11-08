```python
from functools import reduce
from operator import itemgetter

def consolidated(lst):
    def go(abetc, xy):
        if not abetc:
            return [xy]
        a, b = abetc[0]
        etc = abetc[1:]
        x, y = xy
        if y >= b:
            return [xy] + etc
        elif y >= a:
            return [(x, b)] + etc
        else:
            return [xy] + abetc
    def ab(pair):
        a, b = pair
        return (a, b) if a <= b else (b, a)
    
    return reduce(go, sorted(map(ab, lst), key=itemgetter(1)), [])

tests = [
    [],
    [(1.1, 2.2)],
    [(6.1, 7.2), (7.2, 8.3)],
    [(4, 3), (2, 1)],
    [(4, 3), (2, 1), (-1, -2), (3.9, 10)],
    [(1, 3), (-6, -1), (-4, -5), (8, 2), (-6, -6)]
]

def tabulated(s, xShow, fxShow, f, xs):
    def rjust(n, c, s):
        return s.rjust(n, c)
    w = len(max(map(xShow, xs), key=len))
    return '\n'.join([
        s,
        *map(lambda x: rjust(w, ' ', xShow(x)) + ' -> ' + fxShow(f(x)), xs)
    ])

def showPairs(xs):
    if not xs:
        return "[]"
    return '[' + ', '.join(map(showPair, xs)) + ']'

def showPair(pair):
    a, b = pair
    return f'({showNum(a)}, {showNum(b)})'

def showNum(n):
    return str(round(n) if n - round(n) == 0 else n)

print(tabulated("Range consolidations:", str, showPairs, consolidated, tests))
```