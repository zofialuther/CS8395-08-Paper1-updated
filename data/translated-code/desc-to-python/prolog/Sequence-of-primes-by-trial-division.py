def is_prime(n):
    if n in [2, 3, 5]:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(7, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def wheel(n):
    wheel = [1]
    increment = [4, 2, 4, 2, 4, 6, 2, 6]
    for i in range(1, n):
        for j in range(8):
            if sum(wheel) + increment[j] * (i + 1) <= n:
                wheel.append(increment[j])
    return wheel

def wheel_sieve(limit):
    primes = [2, 3, 5]
    wheel = wheel(limit)
    for num in range(7, limit, 2):
        if wheel[num % len(wheel)] == 1:
            if is_prime(num):
                primes.append(num)
    return primes

def accumulator(data):
    for item in data:
        yield item