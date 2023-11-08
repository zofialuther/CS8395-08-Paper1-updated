```python
def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

anti_primes = []
number = 1
while len(anti_primes) < 20:
    divisors = count_divisors(number)
    if all(divisors > count_divisors(x) for x in anti_primes):
        anti_primes.append((number, divisors))
    number += 1

for num, div in anti_primes:
    print(f"Number: {num}, Divisors: {div}")
```