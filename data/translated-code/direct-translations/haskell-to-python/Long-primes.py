```python
def sieve(xs):
    if xs:
        p = xs[0]
        return [p] + sieve([x for x in xs[1:] if x % p != 0])
    else:
        return []

def long_primes_up_to(n):
    def is_long_prime(m):
        cycles = [((10 * k) % m) for k in range(n)]
        index = cycles[1:].index(cycles[0]) if cycles[0] in cycles[1:] else -1
        return n - index == 2 if index != -1 else False

    primes = sieve(list(range(2, n)))
    return list(filter(is_long_prime, primes))

def display(n):
    while n <= 64000:
        print(str(n) + " is " + str(len(long_primes_up_to(n)))
        n *= 2

if __name__ == "__main__":
    five_hundred = long_primes_up_to(500)
    print("The long primes up to 500 are:\n" + str(five_hundred) + "\n")
    print("500 is " + str(len(five_hundred))
    display(1000)
```