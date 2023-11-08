def prime_test_per_requirements(N):
    coefficients = coefficients(N, [1])
    for coefficient in coefficients:
        if coefficient % N != 0:
            return False
    return True