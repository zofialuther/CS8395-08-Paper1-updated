```python
def chowla(n):
    return sum([i for i in range(1, n) if n % i == 0]) - n

def is_prime(num):
    return chowla(num) == 1

def primes_to(limit):
    count = 0
    for i in range(2, limit):
        if is_prime(i):
            count += 1
    return count

def perfect_between(start, end):
    count = 0
    for i in range(start, end+1):
        if chowla(i) == 2*i:
            count += 1
    return count

print(chowla(28))
print(is_prime(11))
print(primes_to(30))
print(perfect_between(1, 10000))
```