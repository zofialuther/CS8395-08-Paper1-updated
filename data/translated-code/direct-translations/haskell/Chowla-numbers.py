```python
from concurrent.futures import ThreadPoolExecutor
import math
import primefac

def chowla(n):
    if n == 1:
        return 0
    else:
        return f(n)

def f(n):
    return - (pred(math.prod(map(sumFactor, primefac.primefac(n)))))

def sumFactor(factor):
    n, e = factor
    return sum([math.pow(prime, p) for p in range(1, e + 1)])

def chowlas(xs):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(lambda x: (x, chowla(x)), xs))

def chowlaPrimes(chowlas, range):
    def isPrime(pair):
        count, n = pair
        if count == 1:
            return False
        else:
            return n == 0
    def count(chowlas):
        return len(list(filter(isPrime, between(range, chowlas))))
    def between(range, chowlas):
        return list(chowlas[range[0] - 1:range[1] - 1])
    return (count(chowlas), range[1])

def chowlaPerfects(chowlas):
    def isPerfect(pair):
        n, c = pair
        if n == 1:
            return False
        else:
            return c == pred(n)
    return list(map(lambda x: x[0], filter(isPerfect, chowlas)))

def commas(a):
    return ','.join(reversed([a[i:i + 3] for i in range(0, len(a), 3)]))

def main():
    cores = math.ceil(math.log2(os.cpu_count()))
    printf("Using %d cores\n" % cores)

    for x, y in chowlas(list(range(1, 38))):
        printf("chowla(%2d) = %d\n" % (x, y))

    for x, y in chowlaP([(1, 10**2), (10**2 + 1, 10**3), (10**3 + 1, 10**4), (10**4 + 1, 10**5), (10**5 + 1, 10**6), (10**6 + 1, 10**7)]):
        printf("There are %8s primes < %10s\n" % (x, commas(str(y))))

    perfects = chowlaPerfects(allChowlas)
    for p in perfects:
        printf("%10s is a perfect number.\n" % commas(str(p)))
    printf("There are %2d perfect numbers < 35,000,000\n" % len(perfects))

def chowlaP(chowlas):
    total = 0
    result = []
    for count, max in chowlas:
        total += count
        result.append((commas(str(total)), commas(str(max))))
    return result

if __name__ == "__main__":
    main()
```