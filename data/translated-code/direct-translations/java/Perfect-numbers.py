from math import isqrt

def perf(n):
    sum = 0
    for i in range(1, int(isqrt(n)) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum == n