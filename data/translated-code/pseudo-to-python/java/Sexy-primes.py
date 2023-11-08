def sieve():
    MAX = 1000035
    primes = [False] * MAX
    for i in range(2, MAX):
        primes[i] = True
    for i in range(2, MAX):
        if primes[i]:
            for j in range(2*i, MAX, i):
                primes[j] = False

def main():
    sieve()
    pairs = 0
    triples = 0
    quadruplets = 0
    unsexyCount = 0
    pairList = []
    tripleList = []
    quadrupletList = []
    unsexyList = []
    for i in range(3, MAX):
        if i-6 >= 3 and primes[i-6] and primes[i]:
            pairs += 1
            pairList.append(str(i-6) + " " + str(i))
            if len(pairList) > 5:
                pairList.pop(0)
        elif i < MAX-2 and primes[i] and (i+6 < MAX and primes[i+6] and not primes[i+6]):
            unsexyCount += 1
            unsexyList.append(i)
            if len(unsexyList) > 10:
                unsexyList.pop(0)
        if i-12 >= 3 and primes[i-12] and primes[i-6] and primes[i]:
            triples += 1
            tripleList.append(str(i-12) + " " + str(i-6) + " " + str(i))
            if len(tripleList) > 5:
                tripleList.pop(0)
        if i-16 >= 3 and primes[i-18] and primes[i-12] and primes[i-6] and primes[i]:
            quadruplets += 1
            quadrupletList.append(str(i-18) + " " + str(i-12) + " " + str(i-6) + " " + str(i))
            if len(quadrupletList) > 5:
                quadrupletList.pop(0)
    print(f"Sexy pairs count: {pairs}, list: {pairList}")
    print(f"Triples count: {triples}, list: {tripleList}")
    print(f"Quadruplets count: {quadruplets}, list: {quadrupletList}")
    print(f"Unsexy primes count: {unsexyCount}, list: {unsexyList}")