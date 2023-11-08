def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def attractiveNumbers(limit):
    primes = [i for i in range(2, limit) if is_prime(i)]
    result = []
    for prime in primes:
        factors = prime_factors(prime)
        if is_prime(len(factors)):
            result.append(prime)
    return result

def main():
    print(attractiveNumbers(120))

main()