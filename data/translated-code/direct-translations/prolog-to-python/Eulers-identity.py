```python
import io
import math

def reduce(A):
    B = simplify(A)
    if B == A:
        return A
    else:
        print(f'= {B}')
        return reduce(B)

def simplify(A):
    if A.startswith("exp(i*X)"):
        return "cos(X) + i*sin(X)"
    elif A == "0 + A":
        return A[-1]
    elif A == "A + 0":
        return A[0]
    elif "+" in A:
        parts = A.split("+")
        if parts[0].isnumeric() and parts[1].isnumeric():
            return str(int(parts[0]) + int(parts[1]))
        else:
            return simplify(parts[0]) + " + " + simplify(parts[1])
    elif "*" in A:
        parts = A.split("*")
        if parts[0] == "0" or parts[1] == "0":
            return "0"
        elif parts[0] == "1":
            return parts[1]
        elif parts[1] == "1":
            return parts[0]
        elif parts[0].isnumeric() and parts[1].isnumeric():
            return str(int(parts[0]) * int(parts[1]))
        else:
            return simplify(parts[0]) + " * " + simplify(parts[1])
    elif A == "cos(0)":
        return "1"
    elif A == "sin(0)":
        return "0"
    elif A == "cos(pi)":
        return "-1"
    elif A == "sin(pi)":
        return "0"
    else:
        return A

A = "exp(i*X)"
C = reduce(A)
print(C)
```