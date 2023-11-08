import random

def isSortedBy(f, xs):
    if len(xs) == 0:
        return True
    else:
        for i in range(len(xs) - 1):
            if not f(xs[i], xs[i+1]):
                return False
        return True

def shuffle(xs):
    n = len(xs)
    ar = xs.copy()
    for i in range(n):
        j = random.randint(i, n-1)
        ar[i], ar[j] = ar[j], ar[i]
    return ar

def bogosortBy(f, xs):
    if isSortedBy(f, xs):
        return xs
    else:
        shuffled_xs = shuffle(xs)
        return bogosortBy(f, shuffled_xs)

def bogosort(xs):
    return bogosortBy(lambda x, y: x < y, xs)