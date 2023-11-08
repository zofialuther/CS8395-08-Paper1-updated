```python
def expand_x_1(n):
    for i in range(n+1):
        yield nCr(n, i)

def aks(p):
    for coeff in expand_x_1(p):
        if coeff % p != 0:
            return False
    return True
```