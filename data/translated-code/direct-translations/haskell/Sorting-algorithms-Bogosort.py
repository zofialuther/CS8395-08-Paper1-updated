import random
import array
from numpy import random
import numpy as np

def isSortedBy(f, xs):
    if not xs:
        return True
    else:
        return all(f(x, y) for x, y in zip(xs, xs[1:]))

def shuffle(xs):
    n = len(xs)
    ar = array.array('i', xs)
    for i in range(n):
        j = np.random.randint(i, n)
        vi = ar[i]
        vj = ar[j]
        ar[j] = vi
        ar[i] = vj
    return ar.tolist()

def bogosortBy(f, xs):
    if isSortedBy(f, xs):
        return xs
    else:
        return bogosortBy(f, shuffle(xs))

def bogosort(xs):
    return bogosortBy(lambda x, y: x < y, xs)