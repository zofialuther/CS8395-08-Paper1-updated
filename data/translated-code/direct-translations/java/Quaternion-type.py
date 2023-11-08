class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def norm(self):
        return (self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2) ** 0.5

    def negative(self):
        return Quaternion(-self.a, -self.b, -self.c, -self.d)

    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def add(self, r):
        return Quaternion(self.a + r, self.b, self.c, self.d)

    def add_quaternion(self, q):
        return Quaternion(self.a + q.a, self.b + q.b, self.c + q.c, self.d + q.d)

    def times(self, r):
        return Quaternion(self.a * r, self.b * r, self.c * r, self.d * r)

    def times_quaternion(self, q):
        return Quaternion(
            self.a * q.a - self.b * q.b - self.c * q.c - self.d * q.d,
            self.a * q.b + self.b * q.a + self.c * q.d - self.d * q.c,
            self.a * q.c - self.b * q.d + self.c * q.a + self.d * q.b,
            self.a * q.d + self.b * q.c - self.c * q.b + self.d * q.a
        )

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def __str__(self):
        return "%.2f + %.2fi + %.2fj + %.2fk" % (self.a, self.b, self.c, self.d)

    def to_quadruple(self):
        return "(%.2f, %.2f, %.2f, %.2f)" % (self.a, self.b, self.c, self.d)

if __name__ == "__main__":
    q = Quaternion(1.0, 2.0, 3.0, 4.0)
    q1 = Quaternion(2.0, 3.0, 4.0, 5.0)
    q2 = Quaternion(3.0, 4.0, 5.0, 6.0)
    r = 7.0
    print("q       = ", q)
    print("q1      = ", q1)
    print("q2      = ", q2)
    print("r       = %.2f\n" % r)
    print("|q|     = %.2f" % q.norm())
    print("-q      = ", q.negative())
    print("q*      = ", q.conjugate())
    print("q + r   = ", q.add(r))
    print("q1 + q2 = ", q1.add_quaternion(q2))
    print("q * r   = ", q.times(r))
    q1q2 = q1.times_quaternion(q2)
    q2q1 = q2.times_quaternion(q1)
    print("q1 * q2 = ", q1q2)
    print("q2 * q1 = ", q2q1)
    print("q1 * q2 %s q2 * q1" % ("=" if q1q2 == q2q1 else "≠"))