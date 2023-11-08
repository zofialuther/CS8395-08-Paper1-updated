```python
from Control.Monad import guard
from Data.List import intercalate
from Data.List.Split import chunksOf
from Math.NumberTheory.Primes import Prime, unPrime, nextPrime
from Math.NumberTheory.Primes.Testing import isPrime
from Text.Printf import printf

data PierPointKind = First | Second

def merge(a, b):
    if not a:
        return b
    elif a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def nSmooth(p):
    factors = []
    for prime in map(unPrime, [nextPrime(1)]):
        if prime <= p:
            factors.append(prime)
        else:
            break
    s = [1]
    for n in factors:
        s = merge(s, [n*x for x in [1] + s])
    return s

def pierpoints(k):
    result = []
    for n in nSmooth(3):
        if k == First:
            x = n + 1
        else:
            x = n - 1
        if isPrime(x):
            result.append(x)
    return result

def main():
    print("\nFirst 50 Pierpont primes of the first kind:\n")
    for row in chunksOf(10, take(50, pierpoints(First))):
        for val in row:
            printf("%12s" % commas(val))
        print("\n")
    print("\nFirst 50 Pierpont primes of the second kind:\n")
    for row in chunksOf(10, take(50, pierpoints(Second))):
        for val in row:
            printf("%12s" % commas(val))
        print("\n")
    print("\n250th Pierpont prime of the first kind: %s\n" % commas(pierpoints(First)[249]))
    print("\n250th Pierpont prime of the second kind: %s\n\n" % commas(pierpoints(Second)[249]))

def rows(lst):
    return chunksOf(10, lst)

def commas(val):
    return ','.join(chunksOf(3, str(val)[::-1]))[::-1]

if __name__ == "__main__":
    main()
```