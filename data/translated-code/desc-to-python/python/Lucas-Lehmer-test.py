```python
def is_prime(n):
    # function to check if a number is prime
    pass

def is_mersenne_prime(p):
    # function to check if a number is a Mersenne prime
    pass

MP = 10  # precision for number of decimal places
upper_bound = 1000  # calculate upper bound for prime numbers
mersenne_primes = []

for p in range(2, upper_bound):
    if is_prime(p):
        if is_mersenne_prime(p):
            mersenne_primes.append(p)

print("Mersenne primes found within the range:", mersenne_primes)
```