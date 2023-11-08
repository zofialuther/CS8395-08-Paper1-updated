from decimal import Decimal, getcontext
import math
import array
from fractions import Fraction

getcontext().prec = 256

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Frac:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("d must not be zero")
        nn = n
        dd = d
        if nn == 0:
            dd = 1
        elif dd < 0:
            nn = -nn
            dd = -dd
        g = abs(gcd(nn, dd))
        if g > 1:
            nn //= g
            dd //= g
        self.num = nn
        self.denom = dd

    @classmethod
    def ZERO(cls):
        return cls(0, 1)

    def __add__(self, rhs):
        return Frac(self.num * rhs.denom + self.denom * rhs.num, rhs.denom * self.denom)

    def __neg__(self):
        return Frac(-self.num, self.denom)

    def __sub__(self, rhs):
        return self + (-rhs)

    def __mul__(self, rhs):
        return Frac(self.num * rhs.num, self.denom * rhs.denom)

    def __lt__(self, other):
        diff = self.toDouble() - other.toDouble()
        return diff < 0

    def __eq__(self, other):
        return isinstance(other, Frac) and self == other

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        return f"{self.num}/{self.denom}"

    def toDouble(self):
        return self.num / self.denom

    def toDecimal(self):
        return Decimal(self.num) / Decimal(self.denom)

def bernoulli(n):
    if n < 0:
        raise ValueError("n may not be negative or zero")
    a = [Frac.ZERO() for _ in range(n + 1)]
    for m in range(n + 1):
        a[m] = Frac(1, m + 1)
        for j in range(m, 0, -1):
            a[j - 1] = (a[j - 1] - a[j]) * Frac(j, 1)
    if n != 1:
        return a[0]
    return -a[0]

def binomial(n, k):
    if n < 0 or k < 0 or n < k:
        raise ValueError
    if n == 0 or k == 0:
        return 1
    num = math.prod(range(k + 1, n + 1))
    den = math.prod(range(2, n - k + 1))
    return num // den

def faulhaberTriangle(p):
    coeffs = [Frac.ZERO() for _ in range(p + 1)]
    q = Frac(1, p + 1)
    sign = -1
    for j in range(p + 1):
        sign *= -1
        coeffs[p - j] = q * Frac(sign, 1) * Frac(binomial(p + 1, j), 1) * bernoulli(j)
    return coeffs

def main():
    for i in range(10):
        coeffs = faulhaberTriangle(i)
        for coeff in coeffs:
            print(f"{coeff:5}  ", end="")
        print()
    print()
    k = 17
    cc = faulhaberTriangle(k)
    n = 1000
    nn = Decimal(n)
    np = Decimal(1)
    total_sum = Decimal(0)
    for c in cc:
        np *= nn
        total_sum += np * c.toDecimal()
    print(total_sum.to_integral_value())

if __name__ == "__main__":
    main()