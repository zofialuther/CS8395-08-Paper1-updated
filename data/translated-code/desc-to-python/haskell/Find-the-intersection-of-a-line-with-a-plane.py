```python
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Implementations for Functor, Applicative, and Num instances

def dot_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

def intersection_point(ray, plane):
    # Implementation of intersection calculation

def main():
    # Implementation of main function
```