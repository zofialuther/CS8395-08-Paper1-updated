def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def divs(n):
    for i in range(2, n + 1):
        if n % i == 0 and isPrime(i):
            return [i] + divs(n // i)
    return []

def factorize(n):
    return divs(n) if n > 1 else []