def mersenne_factor(P, F):
    if prime(P):
        for K in range(1, 100001):
            Q = 2 * K * P + 1
            if test_factor(Q, P, F):
                return True
    return False

def test_factor(Q, P, F):
    if Q*Q > (1 << P - 1):
        return "prime"
    else:
        R = Q & 7
        if R in [1, 7] and prime(Q) and pow(2, P, Q) == 1:
            return Q
    return False

def wheel235(L):
    W = [4, 2, 4, 2, 4, 6, 2, 6]
    W = W * (len(L) // len(W) + 1)
    L = [1, 2, 2] + W[:len(L)-3]
    return L

def prime(N):
    if N >= 2:
        W = wheel235([])
        return prime_helper(N, 2, W)
    return False

def prime_helper(N, D, W):
    if D*D > N:
        return True
    elif N % D != 0:
        return prime_helper(N, D + W[0], W[1:])
    else:
        return False, N, D

# Example usage
print(mersenne_factor(3, 11))