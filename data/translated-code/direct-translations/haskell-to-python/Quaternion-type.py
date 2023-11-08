```python
import math

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
        a = self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d
        b = self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c
        c = self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b
        d = self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a
        return Quaternion(a, b, c, d)

    def __neg__(self):
        return Quaternion(-self.a, -self.b, -self.c, -self.d)

    def __abs__(self):
        return Quaternion(math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2), 0, 0, 0)

    def __truediv__(self, other):
        return self * other.__abs__()

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def __repr__(self):
        return f"Q {self.a} {self.b} {self.c} {self.d}"

def realQ(quaternion):
    return quaternion.a

def imagQ(quaternion):
    return [quaternion.b, quaternion.c, quaternion.d]

def quaternionFromScalar(s):
    return Quaternion(s, 0, 0, 0)

def listFromQ(quaternion):
    return [quaternion.a, quaternion.b, quaternion.c, quaternion.d]

def quaternionFromList(lst):
    return Quaternion(lst[0], lst[1], lst[2], lst[3])

def normQ(quaternion):
    return math.sqrt(sum(x**2 for x in listFromQ(quaternion)))

def conjQ(quaternion):
    return Quaternion(quaternion.a, -quaternion.b, -quaternion.c, -quaternion.d)

if __name__ == "__main__":
    q = Quaternion(1, 2, 3, 4)
    q1 = Quaternion(2, 3, 4, 5)
    q2 = Quaternion(3, 4, 5, 6)
    print((Quaternion(0, 1, 0, 0) * Quaternion(0, 0, 1, 0) * Quaternion(0, 0, 0, 1))) # i*j*k; prints "Q -1.0 0.0 0.0 0.0"
    print(q1 * q2 # prints "Q -56.0 16.0 24.0 26.0"
    print(q2 * q1 # prints "Q -56.0 18.0 20.0 28.0"
    print(q1 * q2 == q2 * q1 # prints "False"
    print(imagQ(q)) # prints "[2.0, 3.0, 4.0]"
```