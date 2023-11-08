from math import isqrt
from random import randint

def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    d = (n - 1) // 2
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(d - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True