```python
def find_prime_numbers(N):
    is_prime.clear()
    is_prime[2] = True
    init_sieve(N, 3)
    sieve(N, 3)

def init_sieve(N, P):
    if P > N:
        return
    else:
        is_prime[P] = True
        Q = P + 2
        init_sieve(N, Q)

def sieve(N, P):
    if P * P > N:
        return
    elif P in is_prime:
        S = P * P
        cross_out(S, N, P)
        Q = P + 2
        sieve(N, Q)
    else:
        Q = P + 2
        sieve(N, Q)

def cross_out(S, N, P):
    if S > N:
        return
    elif S in is_prime:
        del is_prime[S]
        Q = S + 2 * P
        cross_out(Q, N, P)
    else:
        Q = S + 2 * P
        cross_out(Q, N, P)

is_prime = {}
```