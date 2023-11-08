```python
class Quaternion:
    def __init__(self, real, i, j, k):
        self.real = real
        self.i = i
        self.j = j
        self.k = k

    def norm(self):
        return (self.real ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2) ** 0.5

    def conjugate(self):
        return Quaternion(self.real, -self.i, -self.j, -self.k)

    def __add__(self, other):
        return Quaternion(self.real + other.real, self.i + other.i, self.j + other.j, self.k + other.k)

    def __sub__(self, other):
        return Quaternion(self.real - other.real, self.i - other.i, self.j - other.j, self.k - other.k)

    def __mul__(self, other):
        real_part = self.real * other.real - self.i * other.i - self.j * other.j - self.k * other.k
        i_part = self.real * other.i + self.i * other.real + self.j * other.k - self.k * other.j
        j_part = self.real * other.j - self.i * other.k + self.j * other.real + self.k * other.i
        k_part = self.real * other.k + self.i * other.j - self.j * other.i + self.k * other.real
        return Quaternion(real_part, i_part, j_part, k_part)

    def __truediv__(self, other):
        conjugate = other.conjugate()
        norm_squared = other.norm() ** 2
        return self * conjugate / norm_squared

    def reciprocal(self):
        norm_squared = self.norm() ** 2
        return self.conjugate() / norm_squared
```