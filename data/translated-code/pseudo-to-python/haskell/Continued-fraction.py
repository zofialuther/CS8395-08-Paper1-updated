from fractions import Fraction

def cf2rat(n):
    def f(a, b):
        return Fraction(a, 1) + (Fraction(b, 1) / f)
    return f

def cf2rat_p(p, s):
    def f(ys):
        for x, y in ys:
            if abs(x - y) < (1 / float(p)):
                return x
        return f(ys)
    return f(map(lambda i: (cf2rat(i, s), cf2rat(1 + i, s)), map(lambda i: 2 ** i, range(0, 10))))

def cf2dec(n):
    def ratstr(l, a):
        d = a.denominator
        t, n = divmod(a.numerator, d)
        def fracstr(l, n, d):
            if l == 0:
                return []
            else:
                t, n1 = divmod(10 * n, d)
                return [str(t)] + fracstr(l - 1, n1, d)
        return str(t) + '.' + ''.join(fracstr(l, n, d))
    return ratstr(n, cf2rat_p(10 ** n, sqrt2))

def main():
    print(cf2dec(200, sqrt2))
    print(cf2dec(200, napier))
    print(cf2dec(200, pie))

main()