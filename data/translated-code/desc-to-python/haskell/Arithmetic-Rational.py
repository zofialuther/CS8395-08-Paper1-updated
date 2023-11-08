```python
from fractions import Fraction

def getSum(n):
    factors = [i for i in range(1, n) if n % i == 0]
    reciprocals = [Fraction(1, i) for i in factors]
    return sum(reciprocals)

N = 4
perfect_numbers = [n for n in range(1, 10000) if getSum(n) == 1]
print(perfect_numbers[:N])
```