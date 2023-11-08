def isPrime(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, n))