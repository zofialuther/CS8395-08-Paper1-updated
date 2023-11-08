import sympy

def generate_primes():
    primes = []
    for i in range(2, 1000000):
        if '0' not in str(i) and sympy.isprime(i):
            primes.append(i)
    return primes

def is_left_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not sympy.isprime(int(num_str[i:])):
            return False
    return True

def is_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str), 0, -1):
        if not sympy.isprime(int(num_str[:i])):
            return False
    return True

def main():
    primes = generate_primes()
    left_truncatable_primes = [prime for prime in primes if is_left_truncatable_prime(prime)]
    right_truncatable_primes = [prime for prime in primes if is_right_truncatable_prime(prime)]
    print(max(left_truncatable_primes))
    print(max(right_truncatable_primes))

main()