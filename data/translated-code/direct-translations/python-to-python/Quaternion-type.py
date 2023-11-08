class Quaternion:
    def __init__(self, real, i, j, k):
        self.real = real
        self.i = i
        self.j = j
        self.k = k

    def norm(self):
        return (self.real**2 + self.i**2 + self.j**2 + self.k**2)**0.5

    def __neg__(self):
        return Quaternion(-self.real, -self.i, -self.j, -self.k)

    def conjugate(self):
        return Quaternion(self.real, -self.i, -self.j, -self.k)

    def __add__(self, other):
        return Quaternion(self.real + other.real, self.i + other.i, self.j + other.j, self.k + other.k)

    def __mul__(self, other):
        real = self.real * other.real - self.i * other.i - self.j * other.j - self.k * other.k
        i = self.real * other.i + self.i * other.real + self.j * other.k - self.k * other.j
        j = self.real * other.j - self.i * other.k + self.j * other.real + self.k * other.i
        k = self.real * other.k + self.i * other.j - self.j * other.i + self.k * other.real
        return Quaternion(real, i, j, k)

    def __truediv__(self, other):
        conjugate = other.conjugate()
        norm_squared = other.norm()**2
        return self * conjugate * (1/norm_squared)

    def reciprocal(self):
        norm_squared = self.norm()**2
        return self.conjugate() * (1/norm_squared)

    def __eq__(self, other):
        return self.real == other.real and self.i == other.i and self.j == other.j and self.k == other.k

    def __repr__(self):
        return f"Quaternion(real={self.real}, i={self.i}, j={self.j}, k={self.k})"

Q = Quaternion

q = Q(1.0, 2.0, 3.0, 4.0)
q1 = Q(2.0, 3.0, 4.0, 5.0)
q2 = Q(3.0, 4.0, 5.0, 6.0)
r = 7

print(q.norm())
print(q1.norm())
print(q2.norm())
print(-q)
print(q.conjugate())
print(r + q)
print(q + r)
print(q1 + q2)
print(q2 + q1)
print(q * r)
print(r * q)
print(q1 * q2)
print(q2 * q1)
assert q1 * q2 != q2 * q1

i, j, k = Q(0,1,0,0), Q(0,0,1,0), Q(0,0,0,1)
print(i*i)
print(j*j)
print(k*k)
print(i*j*k)
print(q1 / q2)
print(q1 / q2 * q2)
print(q2 * q1 / q2)
print(q1.reciprocal() * q1)
print(q1 * q1.reciprocal())