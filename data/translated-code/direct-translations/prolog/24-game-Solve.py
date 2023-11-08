```python
import random

def play24(Len, Range, Goal):
    L, S = game(Len, Range, Goal)
    for item in L:
        my_write(item)
    print(": ", S)

def game(Len, Range, Value):
    L = []
    for _ in range(Len):
        L.append(random.randint(1, Range))
    S = compute(L, Value, [], [])
    return L, S

def choose(Range):
    return random.randint(1, Range)

def write_tree(M, N):
    if len(M) == 1:
        return [M]
    if M[0] == '+':
        return write_tree(M[1], M[2])
    elif M[0] == '-':
        if is_add(M[2]):
            return write_tree(M[1], M[2][1:]) + ['-'] + [')']
        else:
            return write_tree(M[1], M[2]) + ['-']
    elif M[0] in ['*', '/']:
        MS = write_tree(M[1], M[2])
        NS = write_tree(M[2], M[3])
        if is_add(M[1]):
            TempM = ['('] + MS + [')']
        else:
            TempM = MS
        if is_add(M[2]):
            TempN = ['('] + NS + [')']
        else:
            TempN = NS
        return TempM + [M[0]] + TempN

def is_add(M):
    return M[0] in ['+', '-']

def compute(L, Value, CS, S):
    if len(L) == 1:
        S2 = write_tree(S[0], S[1])
        S = ''.join(S2)
        return S
    else:
        M = L[0]
        N = L[1]
        R, CS2, Expr = next_value(M, N, CS, [])
        return compute([R]+L[2:], Value, Expr, S)

def next_value(M, N, CS, CS2):
    R = M + N
    if [M] in CS:
        CS.remove([M])
        M1 = [M]
    else:
        M1 = CS
    if [N] in CS:
        CS.remove([N])
        N1 = [N]
    else:
        N1 = CS
    return R, CS2, [R - ['+', M1, N1]]

def my_write(V):
    print(V, end=' ')
```