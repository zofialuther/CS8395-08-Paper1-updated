def factors(n):
    factors = set()
    factors.add(n)
    factors.add(1)
    test = n - 1
    while test >= int(n ** 0.5):
        if n % test == 0:
            factors.add(test)
            factors.add(n // test)
        test = test - 1
    return factors