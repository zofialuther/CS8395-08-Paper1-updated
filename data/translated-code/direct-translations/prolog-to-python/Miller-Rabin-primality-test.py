```python
import random

def is_prime(N, Ret):
    if N == 1:
        Ret = False
    elif N == 2:
        Ret = True
    elif N == 3:
        Ret = True
    elif N > 3 and N % 2 == 0:
        Ret = False
    elif N > 3 and N % 2 == 1 and N < 341550071728321:
        L = deterministic_witnesses(N)
        Ret = is_mr_prime(N, L)
    elif N > 3:
        Out = random_witnesses(N, 100, [])
        Ret = is_mr_prime(N, Out)

def deterministic_witnesses(N):
    if N < 1373653:
        return [2, 3]
    elif N < 9080191:
        return [31, 73]
    elif N < 25326001:
        return [2, 3, 5]
    elif N < 3215031751:
        return [2, 3, 5, 7]
    elif N < 4759123141:
        return [2, 7, 61]
    elif N < 1122004669633:
        return [2, 13, 23, 1662803]
    elif N < 2152302898747:
        return [2, 3, 5, 7, 11]
    elif N < 3474749660383:
        return [2, 3, 5, 7, 11, 13]
    else:
        return [2, 3, 5, 7, 11, 13, 17]

def random_witnesses(N, K, T):
    if K == 0:
        return T
    else:
        G = N - 2
        H = 1 + random.randint(0, G)
        I = K - 1
        return random_witnesses(N, I, [H] + T)

def find_ds(N):
    A = N - 1
    return find_ds_helper(A, 0)

def find_ds_helper(D, S):
    if D % 2 == 0:
        P = D // 2
        Q = S + 1
        return find_ds_helper(P, Q)
    else:
        return [D, S]

def is_mr_prime(N, As):
    D, S = find_ds(N)
    return outer_loop(N, As, D, S)

def outer_loop(N, As, D, S):
    A = As[0]
    Base = pow(A, D, N)
    result = inner_loop(Base, N, 0, S)
    if result == False:
        return False
    elif result == True and len(As) == 1:
        return True
    else:
        return outer_loop(N, As[1:], D, S)

def inner_loop(Base, N, Loop, S):
    Next_Base = (Base * Base) % N
    Next_Loop = Loop + 1
    if Loop == 0 and Base == 1:
        return True
    elif Base == N - 1:
        return True
    elif Next_Loop == S:
        return False
    else:
        return inner_loop(Next_Base, N, Next_Loop, S)
```