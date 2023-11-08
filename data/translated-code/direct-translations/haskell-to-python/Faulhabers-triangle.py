from typing import List
from fractions import Fraction

def faulhaber(p: int, n: Fraction) -> Fraction:
    return sum((n ** i) * j for i, j in enumerate(faulhaberTriangle[p]))

def faulhaberTriangle() -> List[List[Fraction]]:
    rs = []
    for n in range(0, 10):
        xs = [((n % i) * j) for i, j in enumerate(rs, start=2)]
        rs = [1 - sum(xs)] + xs
    return rs

def justifyRatio(widths: (int, int), n: int, c: str, nd: Fraction) -> str:
    num, den = nd.numerator, nd.denominator
    w = max(n, widths[0] + widths[1] + 2)
    if den == 1:
        return center(w, c, str(num))
    else:
        q, r = divmod(w - 1, 2)
        return justifyRight(q, c, str(num)) + "/" + justifyLeft(q + r, c, str(den))

def justifyLeft(n: int, c: str, s: str) -> str:
    return s[:n] + c * (n - len(s))

def justifyRight(n: int, c: str, s: str) -> str:
    return c * (n - len(s)) + s

def center(n: int, c: str, s: str) -> str:
    q, r = divmod(n - len(s), 2)
    pad = c * q
    return pad + s + pad + c * r

def maxWidths(xss: List[List[Fraction]]) -> (int, int):
    widest = lambda f, xs: max(len(str(f(x))) for x in xs)
    return (widest(lambda x: x.numerator, [item for sublist in xss for item in sublist]), 
            widest(lambda x: x.denominator, [item for sublist in xss for item in sublist]))

def main():
    triangle = faulhaberTriangle()
    widths = maxWidths(triangle)
    for t in triangle:
        print("\n".join(justifyRatio(widths, 8, ' ', nd) for nd in t))
    print(faulhaber(17, Fraction(1000)))