```python
def sieve(xs):
    if xs:
        p = xs[0]
        return [p] + sieve([x for x in xs[1:] if x % p != 0])
    else:
        return []

def longPrimesUpTo(n):
    primes = sieve(range(2, n))
    def isLongPrime(x):
        cycles = [((10 * i) % x) for i in range(x)]
        index = cycles[1:].index(cycles[0]) if cycles[0] in cycles[1:] else -1
        return (x - index) == 2 if index >= 0 else False
    return list(filter(isLongPrime, primes))

def display(n):
    while n <= 64000:
        print(str(n) + " is " + str(len(longPrimesUpTo(n))))
        n *= 2

fiveHundred = longPrimesUpTo(500)
print("The long primes up to 500 are:\n" + str(fiveHundred) + "\n")
print("500 is " + str(len(fiveHundred)))
display(1000)
```