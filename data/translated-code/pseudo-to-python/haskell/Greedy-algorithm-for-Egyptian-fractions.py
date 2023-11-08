def egyptianFraction(n):
    if n < 0:
        return list(map(lambda x: -x, egyptianFraction(-n)))
    elif n == 0:
        return []
    elif x == 1:
        return [n]
    elif x > y:
        newFraction = x // y % 1
        return [newFraction] + egyptianFraction(x % y % y)
    else:
        newFraction = 1 % r
        return [newFraction] + egyptianFraction((-y) % x % (y * r))
    
    x = numerator(n)
    y = denominator(n)
    r = y // x + 1