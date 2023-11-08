```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(primes):
    n = primes[-1] + 1
    while True:
        if is_prime(n):
            return n
        n += 1

def nPrimes(M):
    primes = [2]
    while len(primes) < M:
        next_prime_num = next_prime(primes)
        primes.append(next_prime_num)
    return primes

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def concatenate_list(lst):
    result = ""
    for item in lst:
        result += str(item)
    return result

def take(N, lst):
    return lst[:N]
```