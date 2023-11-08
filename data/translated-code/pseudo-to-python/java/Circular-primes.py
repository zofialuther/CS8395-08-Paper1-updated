from math import isqrt
from itertools import permutations

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def cycle(n):
    n = str(n)
    return int(n[1:] + n[0])

def isCircularPrime(p):
    if not isPrime(p):
        return False
    num = p
    for _ in range(len(str(p))-1):
        num = cycle(num)
        if not isPrime(num):
            return False
    return True

def testRepunit(digits):
    repunit = int('1' * digits)
    if isPrime(repunit):
        print(f"R({digits})")

# print the first 19 circular primes
print("First 19 circular primes:")
p = 2
count = 0
while count < 19:
    if isCircularPrime(p):
        if count > 0:
            print(", ", end="")
        print(p, end="")
        count += 1
    p += 1
print()

# print the next 4 circular primes
repunit = 1
digits = 1
while repunit < p:
    repunit = 10 * repunit + 1
    digits += 1
bignum = int(str(repunit))
count = 0
while count < 4:
    if isPrime(bignum):
        if count > 0:
            print(", ", end="")
        print(f"R({digits})", end="")
        count += 1
    digits += 1
    bignum = int(str(bignum) + '1')
print()

# test specific repunits
testRepunit(5003)
testRepunit(9887)
testRepunit(15073)
testRepunit(25031)