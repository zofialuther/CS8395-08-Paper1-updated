from itertools import accumulate, chain
from operator import mul

def factorial(n):
    result = list(accumulate(chain([1], range(1, n+1)), mul))
    return result[-1]