def sieve(limit, primes):
    c = [False] * limit
    p = 3
    n = 0
    p2 = p * p
    while p2 <= limit:
        for i in range(p2, limit, 2 * p):
            c[i] = True
        p += 2
        while c[p]:
            p += 2
        p2 = p * p
    for i in range(3, limit, 2):
        if not c[i]:
            primes.append(i)

def findPeriod(n):
    r = 1
    period = 0
    for i in range(1, n+1):
        r = (10 * r) % n
    rr = r
    while r != rr:
        r = (10 * r) % n
        period += 1
    return period

numbers = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000]
totals = [0] * len(numbers)
primes = []
longPrimes = []
sieve(64000, primes)
for prime in primes:
    if findPeriod(prime) == prime - 1:
        longPrimes.append(prime)
count = 0
index = 0
for longPrime in longPrimes:
    if longPrime > numbers[index]:
        totals[index] = count
        index += 1
    count += 1
totals[len(numbers) - 1] = count
print("The long primes up to", numbers[0], "are:")
print(longPrimes[:totals[0]])
print("\nThe number of long primes up to:")
for i in range(8):
    print("  ", numbers[i], "is", totals[i])