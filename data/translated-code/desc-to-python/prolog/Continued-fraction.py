```python
import math

def continued_fraction(N, compute_A_B):
    def _continued_fraction(n, A, B):
        if n == 0:
            return A(0)
        else:
            return A(n) + B(n) / _continued_fraction(n-1, A, B)
    return _continued_fraction(N, compute_A_B[0], compute_A_B[1])

def sqrt_2_A(n):
    return 1

def sqrt_2_B(n):
    return 2

def e_A(n):
    return 2 if n % 3 == 1 else 1 if n == 0 else (n+1) // 3 * 2

def e_B(n):
    return 1

def pi_A(n):
    return 1 if n % 2 == 0 else (n+1) // 2 * 2

def pi_B(n):
    return 2 if n % 2 == 0 else 1

print("Square root of 2:", continued_fraction(10, (sqrt_2_A, sqrt_2_B)))
print("Napier's constant (e):", continued_fraction(10, (e_A, e_B)))
print("Pi:", continued_fraction(10, (pi_A, pi_B)))
```