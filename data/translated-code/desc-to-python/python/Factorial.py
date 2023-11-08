import itertools
import operator

def factorial(n):
    return list(itertools.accumulate(range(1, n+1), operator.mul))[-1]