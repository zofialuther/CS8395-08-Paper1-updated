def eqyptianFraction(x):
    def go(x):
        n, d = x
        r = d // n
        if n != 1:
            if n > d:
                return fr(n % d, d) + fr(n // d, 1)
            else:
                return fr(-d % n, d * r) + fr(1, r)
        else:
            return (0, x)
        if n == 0:
            return None
    
    fr = Fraction
    nd = (x.numerator, x.denominator)
    result = unfoldr(go, nd)
    if nd < 0:
        return list(map(negate, result))
    else:
        return result

def maxEqyptianFraction():
    def maxima(v, fx, xs):
        if fx > v:
            return [(nd, fx)]
        else:
            return xs, v if fx == v and nd not in xs
    
    def go():
        iLast = nDigits * '9'
        result = reduce(maxima, [(n, d) for n in enumFromTo(1, iLast) for d in enumFromTo(1 + n, iLast)], [])
        return f.__name__, list(fs), mx
    
    return go

def main():
    ef = eqyptianFraction
    fr = Fraction
    print(ef(3/7))
    print(ef(4/13))
    print(ef(5/121))
    
    i = 10
    print(maxEqyptianFraction()(i))

def Just(x):
    return Maybe(x)

def Nothing():
    return Maybe()

def enumFromTo(m, n):
    return range(m, n+1)

def unfoldr(f, x):
    result = []
    while x:
        res, x = f(x)
        if res:
            result.append(res)
    return result

if __name__ == "__main__":
    main()