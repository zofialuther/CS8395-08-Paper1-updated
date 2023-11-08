```python
from dataclasses import dataclass

@dataclass
class V3:
    x: int
    y: int
    z: int

    def __add__(self, other):
        return V3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return V3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return V3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __neg__(self):
        return V3(-self.x, -self.y, -self.z)

    def __abs__(self):
        return V3(abs(self.x), abs(self.y), abs(self.z))

    def __truediv__(self, other):
        return V3(self.x / other.x, self.y / other.y, self.z / other.z)

def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

def intersect(rayVector, rayPoint, planeNormal, planePoint):
    diff = rayPoint - planePoint
    prod1 = dot(diff, planeNormal)
    prod2 = dot(rayVector, planeNormal)
    prod3 = prod1 / prod2
    return rayPoint - (rayVector * V3(prod3, prod3, prod3))

if __name__ == "__main__":
    rv = V3(0, -1, -1)
    rp = V3(0, 0, 10)
    pn = V3(0, 0, 1)
    pp = V3(0, 0, 5)

    result = intersect(rv, rp, pn, pp)
    print(f"The ray intersects the plane at ({result.x}, {result.y}, {result.z})")
```