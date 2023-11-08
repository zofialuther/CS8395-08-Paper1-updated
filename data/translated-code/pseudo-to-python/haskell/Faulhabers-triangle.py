```python
from data import Ratio

def faulhaber(p, n):
    result = sum(map(lambda x, y: (n ** x) * y, range(1, len(faulhaberTriangle[p])+1), faulhaberTriangle[p]))

faulhaberTriangle = [list(map(lambda rs, n: 1 - sum([((n % i) * r) for i, r in enumerate(rs, 2)]), faulhaberTriangle[1:], range(10)))]

def main():
    triangle = faulhaberTriangle[:10]
    widths = maxWidths(triangle)
    for t in triangle:
        print('\n'.join(map(lambda x: justifyRatio(widths[0], 8, x, ' ', 1), t)))
    print(numerator(faulhaber(17, 1000)))

def justifyRatio(wn, wd, n, c, nd):
    w = max(n, wn + wd + 2)
    if nd.den == 1:
        result = center(w, c, str(nd.num))
    else:
        q, r = divmod(w - 1, 2)
        result = justifyRight(q, c, str(nd.num)) + "/" + justifyLeft(q + r, c, str(nd.den))

def justifyLeft(n, c, s):
    return s[:n].ljust(n, c)

def justifyRight(n, c, s):
    return s.rjust(n, c)

def center(n, c, s):
    q, r = divmod(n - len(s), 2)
    pad = c * q
    return pad + s + pad + c * r

def maxWidths(xss):
    def widest(f, xs):
        return max(map(lambda x: len(str(f(x))), xs))
    return (widest(lambda x: x.numerator, xss), widest(lambda x: x.denominator, xss))
```