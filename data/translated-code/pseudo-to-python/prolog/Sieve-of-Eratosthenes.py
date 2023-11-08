```python
def sieve(N, Primes):
    Primes.append(2)
    composite = set()
    sieve(N, 2, Primes)

def sieve(N, P, Rest):
    sieve_once(P, N)
    if P == 2:
        P2 = P + 1
    else:
        P2 = P + 2
    for I in range(P2, N):
        if I in composite:
            continue
        else:
            sieve(N, I, Rest)

def sieve(N, P, Rest):
    return

def sieve_once(P, N):
    composite = set()
    for IP in range(P, N, P):
        if IP in composite:
            continue
        else:
            composite.add(IP)

def between(Min, Max, By, I):
    if Min <= Max:
        A = Min + By
        if I == Min:
            return
        else:
            between(A, Max, By, I)

composite = set()
```