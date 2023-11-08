def factorize(n):
    result = []
    for p in range(2, n+1):
        if isPrime(p):
            divisors = divs(n, p)
            for d in divisors:
                result.append(d)
    return result

def divs(n, p):
    divisors = []
    while n % p == 0:
        divisors.append(p)
        n = n // p
    return divisors

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True