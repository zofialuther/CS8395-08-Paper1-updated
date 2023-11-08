from fractions import Fraction

pie = list(zip([0] + [i for i in range(1, 1000, 2)], [4] + [i**2 for i in range(1, 1000)]))
sqrt2 = list(zip([1] + [2 for _ in range(1000)], [1 for _ in range(1000)]))
napier = list(zip([2] + [i for i in range(1, 1000)], [1] + [1 for _ in range(1000)]))

def cf2rat(n, s):
    def f(a, b):
        return a + Fraction(b, s)
    return sum([f(a, b) for a, b in s[:n]], Fraction(0, 1))

def cf2rat_p(p, s):
    def f(i):
        return (cf2rat(i, s), cf2rat(i + 1, s))
    i = 0
    while True:
        x, y = f(2**i)
        if abs(x - y) < 1 / p:
            return x
        i += 1

def cf2dec(n, s):
    def ratstr(l, a):
        d = a.denominator
        t, n = divmod(a.numerator, d)
        return str(t) + '.' + fracstr(l, n, d)

    def fracstr(l, n, d):
        if l == 0:
            return ""
        t, n1 = divmod(10 * n, d)
        return str(t) + fracstr(l - 1, n1, d)

    return ratstr(n, cf2rat_p(10 ** n, s))

print(cf2dec(200, sqrt2))
print(cf2dec(200, napier))
print(cf2dec(200, pie))