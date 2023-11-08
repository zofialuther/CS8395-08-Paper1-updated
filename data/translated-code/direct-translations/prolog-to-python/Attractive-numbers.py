```python
from math import sqrt

def prime_factors(N, Factors):
    S = int(sqrt(N))
    prime_factors_recursive(N, Factors, S, 2)

def prime_factors_recursive(N, Factors, S, P):
    if N == 1:
        Factors = []
        return
    if P <= S and N % P == 0:
        M = N // P
        Factors.append(P)
        prime_factors_recursive(M, Factors, S, P)
    elif P <= S:
        prime_factors_recursive(N, Factors, S, P + 1)
    else:
        Factors.append(N)

def is_prime(N):
    if N == 2:
        return True
    if N % 2 == 0:
        return False
    if N > 2:
        S = int(sqrt(N))
        return not is_composite(N, S, 3)

def is_composite(N, S, P):
    if P <= S and N % P == 0:
        return True
    elif P <= S:
        return is_composite(N, S, P + 2)
    else:
        return False

def attractive_number(N):
    Factors = []
    prime_factors(N, Factors)
    Len = len(Factors)
    return is_prime(Len)

def print_attractive_numbers(From, To, C):
    if From > To:
        return
    if attractive_number(From):
        print('%4r' % From, end='')
        if C % 20 == 0:
            print()
        C1 = C + 1
    else:
        C1 = C
    Next = From + 1
    print_attractive_numbers(Next, To, C1)

def main():
    print_attractive_numbers(1, 120, 1)

main()
```