def egyptianFraction(rational_number):
    from fractions import Fraction
    
    result = []
    num = rational_number.numerator
    den = rational_number.denominator
    
    if num < 0:
        result.append(Fraction(-1, abs(num)))
        num = abs(num)
    while num != 0:
        div = -(-den // num)
        result.append(Fraction(1, div))
        num = num * div - den
        den = den * div
    
    return result