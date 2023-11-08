```python
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_partition(N, K, Primes, Min):
    if K == 1 and is_prime(N) and N > Min:
        return True
    if K > 1:
        for P in range(2, N):
            if is_prime(P) and P > Min and P < N:
                K1 = K - 1
                N1 = N - P
                if prime_partition(N1, K1, Primes, P):
                    Primes.insert(0, P)
                    return True

def print_primes(Primes):
    if len(Primes) == 1:
        print(Primes[0])
    else:
        for i in range(len(Primes) - 1):
            print(Primes[i], "+", end=" ")
        print(Primes[-1])

def print_prime_partition(N, K):
    Primes = []
    if prime_partition(N, K, Primes, 1):
        print(N, "=", end=" ")
        print_primes(Primes)
    else:
        print(N, "cannot be partitioned into", K, "primes.")

def main():
    print_prime_partition(99809, 1)
    print_prime_partition(18, 2)
    print_prime_partition(19, 3)
    print_prime_partition(20, 4)
    print_prime_partition(2017, 24)
    print_prime_partition(22699, 1)
    print_prime_partition(22699, 2)
    print_prime_partition(22699, 3)
    print_prime_partition(22699, 4)
    print_prime_partition(40355, 3)

main()
```