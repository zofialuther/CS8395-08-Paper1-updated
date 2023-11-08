def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    maxFactor = int(n ** 0.5)
    for possibleFactor in range(3, maxFactor+1, 2):
        if n % possibleFactor == 0:
            return False
    return True

def findFactorMersenneNumber(primeP):
    if primeP <= 0:
        raise ValueError("IllegalArgumentException")
    bigP = primeP
    m = 2**primeP - 1
    maxFactor = 2**((primeP + 1) // 2)
    twoP = primeP * 2
    possibleFactor = 1
    possibleFactorBits12 = 0
    twoPBits12 = primeP % 4

    while possibleFactor <= maxFactor:
        possibleFactor = possibleFactor + twoP
        possibleFactorBits12 = (possibleFactorBits12 + twoPBits12) % 4
        if possibleFactorBits12 == 0 or possibleFactorBits12 == 3:
            if pow(2, bigP, possibleFactor) == 1:
                return possibleFactor
    return None

def checkMersenneNumber(p):
    if not isPrime(p):
        print("M" + str(p) + " is not prime")
        return
    factor = findFactorMersenneNumber(p)
    if factor is None:
        print("M" + str(p) + " is prime")
    else:
        print("M" + str(p) + " is not prime, has factor " + str(factor))
    return

def main():
    for p in range(1, 51):
        checkMersenneNumber(p)
    checkMersenneNumber(929)

main()