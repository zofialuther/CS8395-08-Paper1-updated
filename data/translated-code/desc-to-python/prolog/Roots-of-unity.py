```python
import cmath

def root(N):
    return cmath.exp(2 * cmath.pi * 1j / N)

def calculate_roots(N):
    Ks = list(range(N-1))
    Rs = list(map(root, Ks))
    return Rs
```