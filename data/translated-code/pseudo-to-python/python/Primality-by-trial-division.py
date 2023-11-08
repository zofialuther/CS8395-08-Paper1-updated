import re

def isprime(n):
    return not re.match(r'^1?$|^(11+?)\1+$', '1' * n)

prime_numbers = [num for num in range(40) if isprime(num)]
print(prime_numbers)