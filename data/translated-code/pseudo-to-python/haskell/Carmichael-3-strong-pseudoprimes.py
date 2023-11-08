def generatePrimesUpTo(n):
    primes = []
    for num in range(2, n+1):
        if all(num%i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    return primes

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def carmichaels():
    primesList = generatePrimesUpTo(61)
    result = []
    for p in primesList:
        for h3 in range(2, p):
            g = h3 + p
            for d in range(1, g):
                if (g * (p - 1)) % d == 0 and (-1 * p * p) % h3 == d % h3:
                    q = 1 + (((p - 1) * g) / d)
                    if isPrime(q):
                        r = 1 + ((p * q) / h3)
                        if isPrime(r) and (q * r) % (p - 1) == 1:
                            result.append((p, q, r))
    return result

def main():
    carmichaelsList = carmichaels()
    for c in carmichaelsList:
        print(c)

main()