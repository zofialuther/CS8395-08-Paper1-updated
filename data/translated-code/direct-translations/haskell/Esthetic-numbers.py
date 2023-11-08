```python
from itertools import accumulate
from functools import reduce
from operator import mul
from itertools import islice

# a predicate for esthetic numbers
def isEsthetic(b):
    def differences(lst):
        return [x - y for x, y in zip(lst, lst[1:])]
    
    return lambda x: all(map(lambda y: abs(y) == 1, differences(toBase(b, x))))

# Monadic solution, inefficient for small bases.
def esthetics_m(b):
    def fromBase(b):
        return lambda lst: reduce(lambda x, y: x * b + y, lst)
    
    differences = lambda n: [[-1, 1]] * n
    firstDigit = list(range(1, b))
    return [fromBase(b)(list(accumulate(x))) for x in differences(0)] * firstDigit

# Much more efficient iterative solution (translation from Python).
# Uses simple list as an ersatz queue.
def esthetics(b):
    q = [(d, d) for d in range(1, b)]
    step = lambda x: (x[0], x[1][1:] + [(x[0]*b + d, d) for d in range(x[1][0]-1, x[1][0]+1) if 0 <= d < b])
    return list(map(lambda x: x[0], islice(iter(lambda: step, (None, q)), 1, None)))

# representation of numbers as digits
def fromBase(b, lst):
    def f(r, d):
        if d < 0 or d >= b:
            raise StopIteration
        else:
            return r * b + d
    return list(accumulate(lst, f))

def toBase(b, n):
    result = []
    while n > 0:
        n, r = divmod(n, b)
        result.append(r)
    return result

def showInBase(b, n):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    return ''.join(digits[x] for x in toBase(b, n))
```