def prime_test_per_requirements(N):
    coefficients = [1] + get_coefficients(N)
    Cs = coefficients[:-1]
    for C in Cs:
        if C % N != 0:
            return False
    return True

def get_coefficients(N):
    # implement the coefficients function here
    pass
