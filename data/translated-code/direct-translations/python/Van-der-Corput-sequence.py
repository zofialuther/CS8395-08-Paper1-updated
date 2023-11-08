from fractions import Fraction
from mpmath import vdc

Fraction.__repr__ = lambda x: '%i/%i' % (x.numerator, x.denominator)
result = [vdc(i, base=Fraction(2)) for i in range(10)]
print(result)