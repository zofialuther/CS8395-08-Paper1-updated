```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

class Frac:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Parameter d may not be zero.")
        nn = n
        dd = d
        if nn == 0:
            dd = 1
        elif dd < 0:
            nn = -nn
            dd = -dd
        g = abs(gcd(nn, dd))
        if g > 0:
            nn = nn // g
            dd = dd // g
        self.num = nn
        self.denom = dd

    def plus(self, rhs):
        return Frac(
            self.num * rhs.denom + self.denom * rhs.num,
            rhs.denom * self.denom
        )

    def unaryMinus(self):
        return Frac(-self.num, self.denom)

    def minus(self, rhs):
        return self.plus(rhs.unaryMinus())

    def compareTo(self, rhs):
        diff = self.toBigDecimal() - rhs.toBigDecimal()
        if diff < 0:
            return -1
        elif diff > 0:
            return 1
        else:
            return 0

    def equals(self, obj):
        if obj == None or type(obj) != Frac:
            return False
        rhs = obj
        return self.compareTo(rhs) == 0

    def toString(self):
        if self.denom == 1:
            return str(self.num)
        else:
            return "{}/{}".format(self.num, self.denom)

    def toBigDecimal(self):
        return self.num / self.denom

    def toEgyptian(self):
        if self.num == 0:
            return [self]
        fracs = []
        if abs(self.num) >= abs(self.denom):
            div = Frac(self.num // self.denom, 1)
            rem = self.minus(div)
            fracs.append(div)
            self.toEgyptian(rem.num, rem.denom, fracs)
        else:
            self.toEgyptian(self.num, self.denom, fracs)
        return fracs

    def toEgyptian(self, n, d, fracs):
        if n == 0:
            return
        n = float(n)
        d = float(d)
        div, rem = divmod(d, n)
        div = int(div)
        if rem > 0:
            div += 1
        fracs.append(Frac(1, div))
        n3 = (-d) % n
        if n3 < 0:
            n3 += n
        d3 = d * div
        f = Frac(n3, d3)
        if f.num == 1:
            fracs.append(f)
            return
        self.toEgyptian(f.num, f.denom, fracs)

def main():
    fracs = [
        Frac(43, 48),
        Frac(5, 121),
        Frac(2014, 59)
    ]
    for frac in fracs:
        lst = frac.toEgyptian()
        first = lst[0]
        if first.denom == 1:
            print(str(frac) + " -> [" + str(first) + "] + ")
        else:
            print(str(frac) + " -> " + str(first))
        for i in range(1, len(lst)):
            print(" + " + str(lst[i]))
        print()
    for r in [98, 998]:
        if r == 98:
            print("\nFor proper fractions with 1 or 2 digits:")
        else:
            print("\nFor proper fractions with 1, 2 or 3 digits:")
        maxSize = 0
        maxSizeFracs = []
        maxDen = 0
        maxDenFracs = []
        sieve = [[False for j in range(r + 2)] for i in range(r + 1)]
        for i in range(1, r):
            for j in range(i + 1, r + 1):
                if sieve[i][j]:
                    continue
                f = Frac(i, j)
                lst = f.toEgyptian()
                listSize = len(lst)
                if listSize > maxSize:
                    maxSize = listSize
                    maxSizeFracs = [f]
                elif listSize == maxSize:
                    maxSizeFracs.append(f)
                listDen = lst[-1].denom
                if listDen > maxDen:
                    maxDen = listDen
                    maxDenFracs = [f]
                elif listDen == maxDen:
                    maxDenFracs.append(f)
                if i < r // 2:
                    k = 2
                    while True:
                        if j * k > r + 1:
                            break
                        sieve[i * k][j * k] = True
                        k += 1
        print("  largest number of items = " + str(maxSize))
        print("fraction(s) with this number : " + str(maxSizeFracs))
        md = str(maxDen)
        print("  largest denominator = " + str(len(md)) + " digits, " + md[:20] + "..." + md[-20:])
        print("fraction(s) with this denominator : " + str(maxDenFracs))

main()
```