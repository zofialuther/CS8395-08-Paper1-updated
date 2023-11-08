```python
class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def norm(self):
        return (self.a**2 + self.b**2 + self.c**2 + self.d**2)**0.5
    
    def negative(self):
        return Quaternion(-self.a, -self.b, -self.c, -self.d)
    
    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)
    
    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    
    def __mul__(self, other):
        q1 = self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d
        q2 = self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c
        q3 = self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b
        q4 = self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a
        return Quaternion(q1, q2, q3, q4)
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d
    
if __name__ == "__main__":
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    
    print(q1.norm())
    print((q1 + q2).conjugate())
    print(q1 * q2)
    print(q1 == q2)
```