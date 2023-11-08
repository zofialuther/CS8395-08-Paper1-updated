def isqrt(n):
    q = list(filter(lambda x: x < n, [2 ** i for i in range(1, n)]))[-1]
    return go(n, 0, q // 2)

def go(z, r, q):
    if q == 0:
        return r
    else:
        t = z - r - q
        if t >= 0:
            return go(t, r // 2 + q, q // 2)
        else:
            return go(z, r // 2, q // 2)

def main():
    print(isqrt(65))
    for i in range(1, 74, 2):
        print(i, isqrt(49 * 7))