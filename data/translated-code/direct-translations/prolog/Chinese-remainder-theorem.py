def chinrest(A, N):
    N.sort()
    Nn = prime(N)
    if len(A) != len(Nn):
        print('Please enter equal length prime numbers only')
        return
    P = product(Nn)
    Mi = [P//ni for ni in Nn]
    Ci = [modinv(mi, ni) - 1 for mi, ni in zip(Mi, Nn)]
    Ac = [mi * (mi_1_mod_ni) for mi, mi_1_mod_ni in zip(Mi, Ci)]
    Ad = [ai * ci for ai, ci in zip(Ac, A)]
    S = sum(Ad)
    return S % P

def prime(Ys):
    primes = []
    for y in Ys:
        if fd_prime(y):
            primes.append(y)
    return primes

def product(Nn):
    P = 1
    for ni in Nn:
        P *= ni
    return P

def modinv(A, B):
    for P in range(B):
        if (A * P) % B == 1:
            return P
    return -1  # If no modular inverse exists

# Example usage
result1 = chinrest([2, 3, 2], [3, 5, 7])  # Output should be 23
result2 = chinrest([2, 3], [5, 13])  # Output should be 42