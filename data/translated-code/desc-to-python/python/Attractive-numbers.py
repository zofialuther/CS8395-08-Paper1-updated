import sympy

def sieve(n):
    return list(sympy.primerange(2, n))

def get_pfct(n):
    return sympy.factorint(n)

primes_list = sieve(110)
pool = [get_pfct(i) for i in range(121)]
prime_factors_count = [len(pfct) for pfct in pool]

for i in range(len(prime_factors_count)):
    if sympy.isprime(prime_factors_count[i]):
        print(i)