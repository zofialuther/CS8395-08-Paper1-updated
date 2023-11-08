```python
class VectorProds:
    class Vector3D:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def dot(self, vec):
            return (self.a * vec.a +
                    self.b * vec.b +
                    self.c * vec.c)

        def cross(self, vec):
            newA = self.b * vec.c - self.c * vec.b
            newB = self.c * vec.a - self.a * vec.c
            newC = self.a * vec.b - self.b * vec.a
            return VectorProds.Vector3D(newA, newB, newC)

        def scalTrip(self, vecB, vecC):
            return self.dot(vecB.cross(vecC))

        def vecTrip(self, vecB, vecC):
            return self.cross(vecB.cross(vecC))

        def __str__(self):
            return "<" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ">"

    a = VectorProds.Vector3D(3, 4, 5)
    b = VectorProds.Vector3D(4, 3, 5)
    c = VectorProds.Vector3D(-5, -12, -13)

    print(a.dot(b))
    print(a.cross(b))
    print(a.scalTrip(b, c))
    print(a.vecTrip(b, c))
```