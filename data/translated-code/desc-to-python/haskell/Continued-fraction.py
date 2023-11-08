```python
from fractions import Fraction
from math import sqrt, e, pi

def convergent(cf):
    conv = Fraction(cf[-1], 1)
    for term in cf[-2::-1]:
        conv = Fraction(term, 1) + 1 / conv
    return conv

def truncate(cf, max_terms, max_error):
    conv = Fraction(cf[-1], 1)
    for i, term in enumerate(cf[-2::-1], 1):
        conv = Fraction(term, 1) + 1 / conv
        if i >= max_terms or abs(conv - sqrt(2)) <= 1/max_error:
            return conv
    return conv

def decimal(cf, precision):
    num, den = 0, 1
    for term in cf[::-1]:
        num, den = term * num + den, num
    return f"{num // den}.{(num % den) * 10**precision // den:0{precision}d}"

if __name__ == "__main__":
    print(decimal([1] * 100, 200))
    print(decimal([2] + [1] * 99, 200))
    print(decimal([3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1], 200))
```