def pell(n):
    x = int(n ** 0.5)
    return go(x, 1, x * 2, 1, 0, 0, 1)

def go(y, z, r, e1, e2, f1, f2):
    y_prime = r * z - y
    z_prime = (n - y_prime * y_prime) // z
    r_prime = (x + y_prime) // z_prime
    e1_prime, e2_prime = e2, e2 * r_prime + e1
    f1_prime, f2_prime = f2, f2 * r_prime + f1
    a, b = f2_prime, e2_prime
    b_prime, a_prime = a, a * x + b
    if a_prime * a_prime - n * b_prime * b_prime == 1:
        return a_prime, b_prime
    else:
        return go(y_prime, z_prime, r_prime, e1_prime, e2_prime, f1_prime, f2_prime)