```python
from sympy import primerange
import math

def get_primes_by_digits(limit):
    primes_by_digits = []
    p = 10
    primes = []
    for prime in primerange(2, limit):
        if prime > p:
            primes_by_digits.append(primes)
            primes = []
            p *= 10
        primes.append(prime)
    return primes_by_digits

def main():
    primes_by_digits = get_primes_by_digits(100000000)
    print("First 100 brilliant numbers:")
    brilliant_numbers = []
    for primes in primes_by_digits:
        n = len(primes)
        for i in range(n):
            prime1 = primes[i]
            for j in range(i, n):
                prime2 = primes[j]
                brilliant_numbers.append(prime1 * prime2)
        if len(brilliant_numbers) >= 100:
            break
    brilliant_numbers.sort()
    for i in range(100):
        c = '\n' if (i + 1) % 10 == 0 else ' '
        print("{:,d}{}".format(brilliant_numbers[i], c))
    print()
    power = 10
    count = 0
    for p in range(1, 2 * len(primes_by_digits)):
        primes = primes_by_digits[p // 2]
        position = count + 1
        min_product = 0
        n = len(primes)
        for i in range(n):
            prime1 = primes[i]
            primes2 = primes[i:n]
            q = math.ceil(power / prime1)
            j = primes2.index(q) if q in primes2 else -1
            if j == -1:
                continue
            prime2 = primes2[j]
            product = prime1 * prime2
            if min_product == 0 or product < min_product:
                min_product = product
            position += j
            if prime1 >= prime2:
                break
        print("First brilliant number >= 10^{} is {:,d} at position {:,d}".format(p, min_product, position))
        power *= 10
        if p % 2 == 1:
            size = len(primes)
            count += size * (size + 1) / 2

if __name__ == "__main__":
    main()
```