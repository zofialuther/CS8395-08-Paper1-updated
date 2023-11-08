def factorize(n):
    result = []
    for p in range(2, n+1):
        if isPrime(p):
            result.extend(divs(n, p))
    return result

def isPrime(p):
    if p < 2:
        return False
    for i in range(2, int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

def divs(n, p):
    result = []
    while n % p == 0:
        result.append(p)
        n = n // p
    return result
