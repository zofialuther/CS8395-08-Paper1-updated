def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def binCoef(n, k):
    return fac(n) // (fac(k) * fac(n - k))

def pascal():
    return list(map(binCoef, range(0, n+1), range(n)))