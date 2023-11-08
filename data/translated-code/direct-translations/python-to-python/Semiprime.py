def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def semiprime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            return True
    return False

print(semiprime(1679))
print([n for n in range(1, 101) if semiprime(n)])