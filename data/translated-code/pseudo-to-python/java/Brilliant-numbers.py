def getPrimesByDigits(limit):
    primeGen = PrimeGenerator(100000, 100000)
    primesByDigits = []
    primes = []
    p = 10
    while p <= limit:
        prime = primeGen.nextPrime()
        if prime > p:
            primesByDigits.append(primes)
            primes = []
            p *= 10
        primes.append(prime)
    return primesByDigits

def main():
    primesByDigits = getPrimesByDigits(100000000)
    print("First 100 brilliant numbers:")
    brilliantNumbers = []
    for primes in primesByDigits:
        n = len(primes)
        for i in range(n):
            prime1 = primes[i]
            for j in range(i, n):
                prime2 = primes[j]
                brilliantNumbers.append(prime1 * prime2)
        if len(brilliantNumbers) >= 100:
            break
    brilliantNumbers.sort()
    for i in range(100):
        c = '\n' if (i + 1) % 10 == 0 else ' '
        print("%,5d%s" % (brilliantNumbers[i], c))
    print("\n")
    power = 10
    count = 0
    for p in range(1, 2 * len(primesByDigits) + 1):
        primes = primesByDigits[p // 2]
        position = count + 1
        minProduct = 0
        n = len(primes)
        for i in range(n):
            prime1 = primes[i]
            primes2 = primes[i:n]
            q = (power + prime1 - 1) // prime1
            j = primes2.index(q) if q in primes2 else -1
            if j == n:
                continue
            if j < 0:
                j = -(j + 1)
            prime2 = primes2[j]
            product = prime1 * prime2
            if minProduct == 0 or product < minProduct:
                minProduct = product
            position += j
            if prime1 >= prime2:
                break
        print("First brilliant number >= 10^%d is %,d at position %,d" % (p, minProduct, position))
        power *= 10
        if p % 2 == 1:
            size = len(primes)
            count += size * (size + 1) // 2