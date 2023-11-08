```python
import math

def proper_divisors(N):
    if N == 1:
        return [1]
    FSQRTN = math.floor(math.sqrt(N))
    return proper_divisors_helper(2, FSQRTN, N, [])

def proper_divisors_helper(M, FSQRTN, N, L):
    if M > FSQRTN:
        return L
    if N % M == 0:
        MO = N // M
        L.extend([M, MO])
        return proper_divisors_helper(M+1, FSQRTN, N, L)
    else:
        return proper_divisors_helper(M+1, FSQRTN, N, L)

def sumList(lst):
    return sum(lst)

def dpa(N, D, P, A):
    if N == 1:
        D.append(1)
        return
    PN = proper_divisors(N)
    SPN = sumList(PN)
    if SPN < N:
        D.append(N)
    elif SPN > N:
        A.append(N)
    else:
        P.append(N)
    dpa(N-1, D, P, A)

def cpuTime():
    return 0  # You need to implement this function

def dpa(N):
    D = []
    P = []
    A = []
    T0 = cpuTime()
    dpa(N, D, P, A)
    Dur = cpuTime() - T0
    LD = len(D)
    LP = len(P)
    LA = len(A)
    print("deficient: " + str(LD))
    print("abundant: " + str(LA))
    print("perfect: " + str(LP))
    print("took " + str(Dur) + " seconds")
```