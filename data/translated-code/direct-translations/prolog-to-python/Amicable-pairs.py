```python
import math
from itertools import combinations

def divisor(N, Divisor):
    UpperBound = round(math.sqrt(N))
    for D in range(1, UpperBound+1):
        if N % D == 0:
            if D == N / D:
                Divisor.append(D)
            else:
                Divisor.append(D)
                Divisor.append(N//D)

def proper_divisor(N, D):
    Divisor = []
    divisor(N, Divisor)
    for d in Divisor:
        if d != N:
            D.append(d)

def assoc_num_divsSum_in_range(Low, High):
    assoc = {}
    for Num in range(Low, High+1):
        DivSum = sum([D for D in range(1, Num) if Num % D == 0])
        assoc[Num] = DivSum
    return assoc

def get_amicable_pair(Assoc):
    pairs = []
    for M, N in combinations(Assoc.keys(), 2):
        if M < N and Assoc[M] == N and Assoc[N] == M:
            pairs.append((M, N))
    return pairs

def amicable_pairs_under_20000():
    Assoc = assoc_num_divsSum_in_range(1, 20000)
    return get_amicable_pair(Assoc)

print(amicable_pairs_under_20000())
```