```python
from dataclasses import dataclass

@dataclass
class V3:
    x: float
    y: float
    z: float

    def __add__(self, other):
        return V3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return V3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return V3(self.x * other.x, self.y * other.y, self.z * other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __truediv__(self, other):
        return V3(self.x / other, self.y / other, self.z / other)

    def __neg__(self):
        return V3(-self.x, -self.y, -self.z)

    def __abs__(self):
        return V3(abs(self.x), abs(self.y), abs(self.z))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def intersect(rayVector, rayPoint, planeNormal, planePoint):
    diff = rayPoint - planePoint
    prod1 = diff.dot(planeNormal)
    prod2 = rayVector.dot(planeNormal)
    prod3 = prod1 / prod2
    return rayPoint - rayVector * prod3

rv = V3(0, -1, -1)
rp = V3(0, 0, 10)
pn = V3(0, 0, 1)
pp = V3(0, 0, 5)

result = intersect(rv, rp, pn, pp)
print(f"The ray intersects the plane at {result}")
```