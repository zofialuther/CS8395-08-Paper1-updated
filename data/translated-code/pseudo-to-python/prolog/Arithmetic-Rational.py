```python
import math

def divisor(N, Div):
    Max = math.floor(math.sqrt(N))
    for D in range(1, Max+1):
        if (N % D == 0):
            if Div == D:
                return True
            elif Div == N // D and Div != D:
                return True
    return False

def divisors(N):
    return {M for M in range(1, N+1) if divisor(N, M)}

def recip(A):
    return 1 / A

def sumrecip(N):
    Divs = divisors(N)
    As = list(map(recip, Divs))
    return sum(As)

def perfect(X):
    return sumrecip(X) == 1

def main():
    Limit = 1 << 19
    for N in range(1, Limit+1):
        if perfect(N):
            print(N)
    return
```