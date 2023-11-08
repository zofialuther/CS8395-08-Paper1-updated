def isPrime(n):
    if n > 1 and all(n % i != 0 for i in range(2, n)):
        return True
    else:
        return False