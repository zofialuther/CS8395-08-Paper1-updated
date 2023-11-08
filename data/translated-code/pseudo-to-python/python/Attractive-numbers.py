from sympy import sieve

def get_pfct(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return len(factors)

primes = list(sieve.primerange(2, 110))
pool = [get_pfct(each) for each in range(121)]

for index, element in enumerate(pool):
    if element in primes:
        print(index)