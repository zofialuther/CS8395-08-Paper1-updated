import numpy as np

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    d = 5
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
        if n % d == 0:
            return False
        d += 4
    return True

def find_combo(k, x, m, n, combo, primes):
    found_combo = False
    if k >= m:
        if np.sum([primes[i] for i in combo]) == x:
            s = 's' if m > 1 else ''
            print(f"Partitioned {x:5d} with {m:2d} prime{s}: ", end='')
            for i in range(m):
                print(primes[combo[i]], end='')
                if i < m - 1:
                    print('+', end='')
                else:
                    print()
            found_combo = True
    else:
        for j in range(n):
            if k == 0 or j > combo[k - 1]:
                combo[k] = j
                if not found_combo:
                    found_combo = find_combo(k + 1, x, m, n, combo, primes)
    return found_combo

def partition(x, m, primes):
    if x < 2 or m < 1 or m >= x:
        raise ValueError
    filtered_primes = [p for p in primes if p <= x]
    n = len(filtered_primes)
    if n < m:
        raise ValueError("Not enough primes")
    combo = [0] * m
    found_combo = find_combo(0, x, m, n, combo, filtered_primes)
    if not found_combo:
        s = 's' if m > 1 else ''
        print(f"Partitioned {x:5d} with {m:2d} prime{s}: (not possible)")

if __name__ == "__main__":
    primes = np.concatenate((np.array([2]), np.fromiter((n for n in range(3, 100000, 2) if is_prime(n)), dtype=int, count=50000)))
    partition(99809, 1, primes)
    partition(18, 2, primes)
    partition(19, 3, primes)
    partition(20, 4, primes)
    partition(2017, 24, primes)
    partition(22699, 1, primes)
    partition(22699, 2, primes)
    partition(22699, 3, primes)
    partition(22699, 4, primes)
    partition(40355, 3, primes)