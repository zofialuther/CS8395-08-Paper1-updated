```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def find_largest_left_truncatable_prime(N):
    for i in range(N - 1, 1, -1):
        if is_prime(i) and is_left_truncatable_prime(i):
            return i
    return -1

def find_largest_right_truncatable_prime(N):
    for i in range(N - 1, 1, -1):
        if is_prime(i) and is_right_truncatable_prime(i):
            return i
    return -1

def main(N):
    primes = [i for i in range(2, N) if is_prime(i)]
    largest_left_truncatable_prime = find_largest_left_truncatable_prime(N)
    largest_right_truncatable_prime = find_largest_right_truncatable_prime(N)
    print("Largest left-truncatable prime less than", N, "is:", largest_left_truncatable_prime)
    print("Largest right-truncatable prime less than", N, "is:", largest_right_truncatable_prime)

N = 1000
main(N)
```