from math import isqrt

def isqrt(n):
    q = 1
    while q * q < n:
        q <<= 2
    r = 0
    while q != 0:
        t = n - r - q
        if t >= 0:
            n = t
            r >>= 1
            r += q
        else:
            r >>= 1
        q >>= 2
    return r

print(list(map(isqrt, range(1, 66))))
for i, j in zip(range(1, 74, 2), map(lambda x: isqrt(x), (49 * x for x in range(7, 74, 7)))):
    print(i, j)