from fractions import Fraction

def egyptianFraction(n):
    if n < 0:
        return [Fraction(-x) for x in egyptianFraction(-n)]
    elif n == 0:
        return []
    else:
        x = n.numerator
        y = n.denominator
        r = y // x + 1
        if x == 1:
            return [n]
        elif x > y:
            return [Fraction(x // y)] + egyptianFraction(Fraction(x % y, y))
        else:
            return [Fraction(1, r)] + egyptianFraction(Fraction((-y) % x, y * r))