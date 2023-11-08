from math import isqrt

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    for p in range(5, isqrt(n) + 1, 6):
        if n % p == 0:
            return False
        if n % (p + 2) == 0:
            return False
    return True

def cycle(n):
    m = n
    p = 1
    while m >= 10:
        p *= 10
        m //= 10
    return m + 10 * (n % p)

def isCircularPrime(p):
    if not isPrime(p):
        return False
    p2 = cycle(p)
    while p2 != p:
        if p2 < p or not isPrime(p2):
            return False
        p2 = cycle(p2)
    return True

def testRepunit(digits):
    repunit = int('1' * digits)
    if isPrime(repunit):
        print(f"R({digits}) is probably prime.")
    else:
        print(f"R({digits}) is not prime.")

def main():
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
    print("Next 4 circular primes:")
    repunit = 1
    digits = 1
    while repunit < p:
        digits += 1
        repunit = 10 * repunit + 1
    for i in range(4):
        if isPrime(repunit):
            if i > 0:
                print(", ", end="")
            print(f"R({digits})", end="")
        digits += 1
        repunit = repunit * 10 + 1
    print()
    testRepunit(5003)
    testRepunit(9887)
    testRepunit(15073)
    testRepunit(25031)

if __name__ == "__main__":
    main()