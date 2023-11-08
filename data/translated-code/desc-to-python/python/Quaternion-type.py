```python
# Implementation of quaternion numbers

class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __sub__(self, other):
        return Quaternion(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)

    def __mul__(self, other):
        return Quaternion(self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d,
                          self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c,
                          self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b,
                          self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a)

    def __truediv__(self, other):
        conjugate = Quaternion(other.a, -other.b, -other.c, -other.d)
        denominator = other.a**2 + other.b**2 + other.c**2 + other.d**2
        return self * conjugate / denominator

    def normalize(self):
        magnitude = (self.a**2 + self.b**2 + self.c**2 + self.d**2)**0.5
        return Quaternion(self.a / magnitude, self.b / magnitude, self.c / magnitude, self.d / magnitude)

    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def reciprocal(self):
        conjugate = self.conjugate()
        denominator = self.a**2 + self.b**2 + self.c**2 + self.d**2
        return conjugate / denominator

# Other operations involving quaternions can also be implemented as needed
```