```python
import heapq

def three_smooth(Lz):
    H = [1]
    heapq.heapify(H)
    next_3smooth(-H, Lz)

def next_3smooth(Top_H0, N_H2, N):
    heapq.heappop(H0)
    _, top = H0[0]
    heapq.heappop(H0)
    _, top2 = H0[0]
    next_3smooth(-top, N_H2, N)
    heapq.heappop(H0)
    _, top3 = H0[0]
    heapq.heappush(H0, (N * 2, None))
    heapq.heappush(H0, (N * 3, None))

def first_kind(K):
    three_smooth(Ns)
    N = next(Ns)
    K = N + 1
    prime(K)

def second_kind(K):
    three_smooth(Ns)
    N = next(Ns)
    K = N - 1
    prime(K)

def show(Seq, N):
    print(f"The first {N} values of {Seq} are: ")
    for i in range(N):
        print(next(Seq))
    print(f"The 250th value of {Seq} is {Seq[249]}")

def main():
    show(first_kind, 50)
    show(second_kind, 50)

def prime(N):
    if isinstance(N, int) and N > 1:
        divcheck(N, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149], Result)
        miller_rabin_primality_test(N)

def divcheck(_, [], "unknown"):
    pass

def divcheck(N, [P], "prime"):
    pass

def divcheck(N, [P], State):
    pass

def miller_rabin_primality_test(N):
    bases([31, 73], N)
    strong_fermat_pseudoprime(N, A)

def miller_rabin_precision(16):
    pass

def bases([31, 73], N):
    pass

def bases([2, 7, 61], N):
    pass

def bases([2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022], N):
    pass

def bases(Bases, N):
    pass

def strong_fermat_pseudoprime(N, A):
    factor_2s(Pn, S, D)
    powm(A, D, N)
    composite_witness(N, S, X)

def composite_witness(_, 0, _):
    pass

def composite_witness(N, K, X):
    factor_2s(N, S, D)
    factor_2s(S, D, S, D)
    factor_2s(S0, D0, S, D)
```