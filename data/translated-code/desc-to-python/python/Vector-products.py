```python
import numpy as np

def crossp(a, b):
    return np.cross(a, b)

def dotp(a, b):
    return np.dot(a, b)

def scalartriplep(a, b, c):
    return np.dot(a, np.cross(b, c))

def vectortriplep(a, b, c):
    return np.cross(a, np.cross(b, c))

if __name__ == "__main__":
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    v3 = np.array([7, 8, 9])

    print("Cross product:", crossp(v1, v2))
    print("Dot product:", dotp(v1, v2))
    print("Scalar triple product:", scalartriplep(v1, v2, v3))
    print("Vector triple product:", vectortriplep(v1, v2, v3))
```