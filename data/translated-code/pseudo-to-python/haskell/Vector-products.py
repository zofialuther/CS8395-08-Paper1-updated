```python
from typing import List

Vector = List[int]
Scalar = int

a: Vector
b: Vector
c: Vector
d: Vector

a = [3, 4, 5]
b = [4, 3, 5]
c = [-5, -12, -13]
d = [3, 4, 5, 6]

def dot(u: Vector, v: Vector) -> Scalar:
    if len(u) == len(v):
        return sum(u_i * v_i for u_i, v_i in zip(u, v))
    else:
        raise ValueError("Dotted Vectors must be of equal dimension.")

def cross(u: Vector, v: Vector) -> Vector:
    if len(u) == 3 and len(v) == 3:
        return [
            u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0]
        ]
    else:
        raise ValueError("Crossed Vectors must both be three dimensional.")

def scalarTriple(q: Vector, r: Vector, s: Vector) -> Scalar:
    return dot(q, cross(r, s))

def vectorTriple(q: Vector, r: Vector, s: Vector) -> Vector:
    return cross(q, cross(r, s))

def main():
    print("a . b     = ", dot(a, b))
    print("a x b     = ", cross(a, b))
    print("a . b x c = ", scalarTriple(a, b, c))
    print("a x b x c = ", vectorTriple(a, b, c))
    print("a . d     = ", dot(a, d))

main()
```