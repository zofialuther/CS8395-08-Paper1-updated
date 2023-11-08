```python
from sympy.ntheory import factorint

def fractran_primes():
    i = 1
    while True:
        fr = fractran(2, i)
        binstr = bin(fr)[2:]
        if binstr.count('1') == 1:
            prime = binstr.count('0')
            if prime > 1:   # Skip 2**0 and 2**1
                yield prime, i
        i += 1

if __name__ == '__main__':
    for (prime, i), j in zip(fractran_primes(), range(15)):
        print("Generated prime %2i from the %6i'th member of the fractran series" % (prime, i))
```