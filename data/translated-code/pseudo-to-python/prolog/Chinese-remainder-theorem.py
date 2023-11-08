def chinrest(A, N, X):
    N.sort()
    Nn = prime(N)
    if not Nn:
        print("Please enter prime numbers only")
        return
    if len(A) != len(Nn):
        print("Please enter equal length prime numbers only")
        return
    P = product(Nn)
    Mi = milist(P, Nn)
    Ci = cilist(Mi, Nn)
    Ac = mult_lists(Mi, Ci)
    Ad = mult_lists(Ac, A)
    S = sum_list(Ad)
    X = S % P

def prime(arr):
    primeArr = []
    for i in range(len(arr)):
        if fd_prime(arr[i]):
            primeArr.append(arr[i])
        else:
            return False
    return primeArr

def product(arr):
    P = 1
    for i in range(len(arr)):
        P *= arr[i]
    return P

def milist(P, arr):
    Mi = []
    for i in range(len(arr)):
        Mi.append(P // arr[i])
    return Mi

def cilist(arr1, arr2):
    Ci = []
    for i in range(len(arr1)):
        Ci.append(modinv(arr1[i], arr2[i]))
    return Ci

def mult_lists(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] * arr2[i])
    return result

def sum_list(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

def modinv(A, B):
    GCD = eeuclid(A, B)
    if GCD != 1:
        return
    return P % B

def eeuclid(A, B):
    if A >= B:
        return a_b_p_s(A, B, 1, 0, 0, 1, A)
    else:
        return a_b_p_s(B, A, 1, 0, 0, 1, A)

def a_b_p_s(A, B, P1, S1, P2, S2, GCD):
    if B == 0:
        return GCD
    if A > B:
        Q = A // B
        B1 = A % B
        P3 = P1 - (Q * P2)
        S3 = S1 - (Q * S2)
        return a_b_p_s(B, B1, P2, S2, P3, S3, GCD)