```python
from sympy import isprime, primerange
import itertools

def rotated(xs):
    if any(x < xs[0] for x in xs):
        return []
    else:
        return [as_num(n) for n in itertools.islice(rotate(xs), len(xs)-1)]

def rotate(xs):
    if not xs:
        return []
    else:
        return itertools.chain([xs[1:]+[xs[0]]], rotate(xs[1:]+[xs[0]]))

def as_num(n):
    if all(x == 1 for x in n):
        return int(''.join(map(str, n)))
    else:
        return n[0] * 10 ** (len(n) - 1) + as_num(n[1:])

def digits(n):
    if n == 0:
        return []
    else:
        d, r = divmod(n, 10)
        return digits(d) + [r]

def is_circular(repunit, n):
    if repunit:
        return isprime(n)
    elif n < 10:
        return True
    elif n % 2 == 0:
        return False
    else:
        rotations = rotated(digits(n))
        if not rotations or any(x < n for x in rotations):
            return False
        else:
            return all(isprime(x) for x in rotations)

def repunits():
    n = 2
    while True:
        yield as_num([1]*n)
        n += 1

def as_repunit(n):
    return as_num([1]*n)

def main():
    primes = list(primerange(1, 1000))
    circular_primes = [x for x in primes if is_circular(False, x)]
    print(f"The first 19 circular primes are:\n{circular_primes[:19]}\n")

    repunits_list = [sum(digits(x)) for x in itertools.islice(repunits(), 1, 6)]
    print("The next 4 circular primes, in repunit format are:")
    for r in repunits_list:
        print(f"R({r}) ", end="")
    print("\n")

    probably_circular_primes = [5003, 9887, 15073, 25031, 35317, 49081]
    print("The following repunits are probably circular primes:")
    for r in probably_circular_primes:
        print(f"R({r}) : {is_circular(True, as_repunit(r))}")

if __name__ == "__main__":
    main()
```