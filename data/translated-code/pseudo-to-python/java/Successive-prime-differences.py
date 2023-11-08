def sieve(limit):
    primes = []
    primes.append(2)
    c = [False] * (limit + 1)
    p = 3
    while True:
        p2 = p * p
        if p2 > limit:
            break
        for i in range(p2, limit + 1, 2 * p):
            c[i] = True
        while c[p]:
            p += 2
    res = []
    for i in range(3, limit + 1, 2):
        if not c[i]:
            primes.append(i)
    return primes

def successivePrimes(primes, diffs):
    results = []
    dl = len(diffs)
    for i in range(len(primes) - dl):
        group = [0] * (dl + 1)
        group[0] = primes[i]
        for j in range(i, i + dl):
            if primes[j + 1] - primes[j] != diffs[j - i]:
                break
            group[j - i + 1] = primes[j + 1]
        else:
            results.append(group)
    return results

primes = sieve(999999)
diffsList = [[2], [1], [2, 2], [2, 4], [4, 2], [6, 4, 2]]
print("For primes less than 1,000,000:-\n")
for diffs in diffsList:
    print("  For differences of " + str(diffs) + " ->\n")
    sp = successivePrimes(primes, diffs)
    if not sp:
        print("    No groups found\n")
        continue
    print("    First group   = " + str(sp[0]) + "\n")
    print("    Last group    = " + str(sp[-1]) + "\n")
    print("    Number found  = " + str(len(sp)) + "\n\n")