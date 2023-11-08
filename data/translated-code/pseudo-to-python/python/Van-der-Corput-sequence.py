from fractions import Fraction

Fraction.__repr__ = lambda x: '%i/%i' % (x.numerator, x.denominator)

result_list = [vdc(i, base=Fraction(2)) for i in range(10)]

print(result_list)