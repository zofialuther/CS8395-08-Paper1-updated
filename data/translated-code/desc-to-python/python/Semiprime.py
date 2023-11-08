def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def semiprime(n):
    for i in range(2, n):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return True
    return False

semiprimes = [x for x in range(1, 101) if semiprime(x)]
print(semiprimes)