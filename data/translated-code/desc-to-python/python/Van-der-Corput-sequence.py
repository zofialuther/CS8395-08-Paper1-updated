```python
from fractions import Fraction

Fraction.__str__ = lambda self: f"{self.numerator}/{self.denominator}"

fractions = [Fraction(int(v, 2)) for v in range(10)]
print(fractions)
```