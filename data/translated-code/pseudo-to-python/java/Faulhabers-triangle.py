import math

class FaulhabersTriangle:
    MC = math.context(256)

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

class Frac:
    ZERO = Frac(0, 1)

    def __init__(self, n, d):
        if d == 0:
            raise ValueError("IllegalArgumentException")
        else:
            nn = n
            dd = d
            if nn == 0:
                dd = 1
            if dd < 0:
                nn = -nn
                dd = -dd
            g = gcd(nn, dd)
            if g > 1:
                nn = nn / g
                dd = dd / g
            self.num = nn
            self.denom = dd

    def plus(self, other):
        pass

    def unaryMinus(self):
        pass

    def minus(self, other):
        pass

    def times(self, other):
        pass

    def compareTo(self, other):
        pass

    def equals(self, other):
        pass

    def toString(self):
        pass

    def toDouble(self):
        pass

    def toBigDecimal(self):
        pass

def bernoulli(n):
    if n < 0:
        raise ValueError("IllegalArgumentException")
    a = [Frac.ZERO] * (n+1)
    for m in range(n+1):
        a[m] = Frac(1, m+1)
        for j in range(m, 0, -1):
            a[j-1] = (a[j-1] - a[j]) * Frac(j, 1)
    if n != 1:
        return a[0]
    else:
        return a[0].unaryMinus()

def binomial(n, k):
    if n < 0 or k < 0 or n < k:
        raise ValueError("IllegalArgumentException")
    if n == 0 or k == 0:
        return 1
    num = 1
    den = 1
    for i in range(k):
        num = num * (n - i)
        den = den * (i + 1)
    return num / den

def faulhaberTriangle(p):
    coeffs = [Frac.ZERO] * (p+1)
    q = Frac(1, p+1)
    sign = -1
    for j in range(p+1):
        sign *= -1
        coeffs[p-j] = q * Frac(sign) * Frac(binomial(p+1, j)) * bernoulli(j)
    return coeffs

def main():
    for i in range(10):
        coeffs = faulhaberTriangle(i)
        for coeff in coeffs:
            print(coeff)
        print()
    k = 17
    cc = faulhaberTriangle(k)
    n = 1000
    nn = BigDecimal(n)
    np = BigDecimal(1)
    sum = BigDecimal(0)
    for c in cc:
        np = np * nn
        sum = sum + np * c.toBigDecimal()
    print(int(sum))