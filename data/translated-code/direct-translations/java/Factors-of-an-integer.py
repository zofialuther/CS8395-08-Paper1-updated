def factors(n):
    factors = {n}
    factors.add(1)
    for test in range(n-1, int(n**0.5), -1):
        if n % test == 0:
            factors.add(test)
            factors.add(n // test)
    return factors