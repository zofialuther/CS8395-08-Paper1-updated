def chowla(n):
    if n == 1:
        return 0
    else:
        return f(n)

def f(n):
    factor_list = factorise(n)
    product = 1
    for factor in factor_list:
        factor_sum = 0
        for i in range(1, factor[1]+1):
            factor_sum = factor_sum + unPrime(factor[0])**i
        product = product * factor_sum
    return product - (product - 1)

def sumFactor(n, e):
    factor_sum = 0
    for i in range(1, e+1):
        factor_sum = factor_sum + unPrime(n)**i
    return factor_sum

def chowlas(xs):
    if not xs:
        return []
    else:
        chunks = chunksOf(10**6, xs)
        par_result = runPar(join(mapM(spawnP(fmap((,) <*> chowla), chunks)))
        return mapM(get, par_result)

def chowlaPrimes(chowlas, range):
    def isPrime(n, m):
        if n == 1:
            return False
        else:
            return m == 0
    
    def count(chowlas):
        count = 0
        for pair in chowlas:
            if isPrime(pair[0], pair[1]):
                count = count + 1
        return count

    def between(min, max):
        return genericTake(max - (min - 1), genericDrop(min - 1))
    
    return (count(chowlas), range[0])

def chowlaPerfects(chowlas):
    def isPerfect(n, c):
        if n == 1:
            return False
        else:
            return c == (n - 1)
    
    return filter(isPerfect, chowlas)

def commas(a):
    string = reverse(intercalate(",", chunksOf(3, reverse(show(a)))))
    return string

def main():
    cores = getNumProcessors()
    setNumCapabilities(cores)
    printf("Using %d cores\n", cores)

    for pair in take(37, allChowlas):
        printf("chowla(%2d) = %d\n", pair[0], pair[1])

    for range in chowlaP([(1, 10**2), (10**2 + 1, 10**3), (10**3 + 1, 10**4), (10**4 + 1, 10**5), (10**5 + 1, 10**6), (10**6 + 1, 10**7)]):
        printf("There are %8s primes < %10s\n", range[0], range[1])

    for perfect in perfects:
        printf("%10s is a perfect number.\n", commas(perfect))

    printf("There are %2d perfect numbers < 35,000,000\n", length(perfects))