from sympy import primerange, isprime

primes1e6 = list(filter(lambda x: '0' not in str(x), list(primerange(2, 1000000)))[::-1])

def rightT(n):
    while n > 0:
        if not isprime(n):
            return False
        n = n // 10
    return True

def leftT(n):
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[1:])
    return True

ltp = next(filter(leftT, primes1e6))
rtp = next(filter(rightT, primes1e6))

print("Left truncatable ", ltp)
print("Right truncatable ", rtp)