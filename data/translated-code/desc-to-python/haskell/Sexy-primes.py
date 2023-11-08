```python
from sympy import primerange

class Group:
    def __init__(self, pairs, triplets, quadruplets, quintuplets, unsexy):
        self.pairs = pairs
        self.triplets = triplets
        self.quadruplets = quadruplets
        self.quintuplets = quintuplets
        self.unsexy = unsexy

def collect_prime_groups(limit):
    primes = list(primerange(1, limit))
    pairs = [primes[i:i+2] for i in range(len(primes)-1) if primes[i+1] - primes[i] == 2]
    triplets = [primes[i:i+3] for i in range(len(primes)-2) if primes[i+1] - primes[i] == 2 and primes[i+2] - primes[i+1] == 2]
    quadruplets = [primes[i:i+4] for i in range(len(primes)-3) if primes[i+1] - primes[i] == 2 and primes[i+2] - primes[i+1] == 2 and primes[i+3] - primes[i+2] == 2]
    quintuplets = [primes[i:i+5] for i in range(len(primes)-4) if primes[i+1] - primes[i] == 2 and primes[i+2] - primes[i+1] == 2 and primes[i+3] - primes[i+2] == 2 and primes[i+4] - primes[i+3] == 2]
    unsexy = [prime for prime in primes if prime % 6 != 1]
    return Group(pairs, triplets, quadruplets, quintuplets, unsexy)

def main():
    limit = 1000035
    groups = collect_prime_groups(limit)
    print("Number of pairs:", len(groups.pairs))
    print("Number of triplets:", len(groups.triplets))
    print("Number of quadruplets:", len(groups.quadruplets))
    print("Number of quintuplets:", len(groups.quintuplets))
    print("Last few elements in pairs:", groups.pairs[-5:])
    print("Last few elements in triplets:", groups.triplets[-5:])
    print("Last few elements in quadruplets:", groups.quadruplets[-5:])
    print("Last few elements in quintuplets:", groups.quintuplets[-5:])
    print("Unsexy prime numbers:", groups.unsexy)

if __name__ == "__main__":
    main()
```