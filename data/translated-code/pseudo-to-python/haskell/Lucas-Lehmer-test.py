def sieve(primeList):
    outputList = []
    for p in primeList:
        outputList.append(p)
        for x in primeList:
            if x % p > 0:
                primeList.append(x)
    return outputList