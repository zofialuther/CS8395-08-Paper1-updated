```python
import numpy as np

def dot_product(vector1, vector2):
    return np.dot(vector1, vector2)

def cross_product(vector1, vector2):
    return np.cross(vector1, vector2)

def scalar_triple_product(vector1, vector2, vector3):
    return np.dot(vector1, np.cross(vector2, vector3))

def vector_triple_product(vector1, vector2, vector3):
    return np.cross(vector1, np.cross(vector2, vector3))
```