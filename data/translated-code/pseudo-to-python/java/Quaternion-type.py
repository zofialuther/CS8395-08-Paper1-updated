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
    
    def add(self, q):
        return Quaternion(self.a + q.a, self.b + q.b, self.c + q.c, self.d + q.d)
    
    @staticmethod
    def add(q, r):
        return q.add(r)
    
    @staticmethod
    def add(r, q):
        return q.add(r)
    
    def times(self, r):
        return Quaternion(self.a * r, self.b * r, self.c * r, self.d * r)
    
    @staticmethod
    def times(q, r):
        return q.times(r)
    
    @staticmethod
    def times(r, q):
        return q.times(r)
    
    def times(self, q):
        return Quaternion(
            self.a * q.a - self.b * q.b - self.c * q.c - self.d * q.d,
            self.a * q.b + self.b * q.a + self.c * q.d - self.d * q.c,
            self.a * q.c - self.b * q.d + self.c * q.a + self.d * q.b,
            self.a * q.d + self.b * q.c - self.c * q.b + self.d * q.a
        )
    
    @staticmethod
    def times(q1, q2):
        return q1.times(q2)
    
    def __eq__(self, obj):
        if not isinstance(obj, Quaternion):
            return False
        other = obj
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c, other.d)
    
    def __str__(self):
        return "{:.2f} + {:.2f}i + {:.2f}j + {:.2f}k".format(self.a, self.b, self.c, self.d).replace("+ -", "- ")
    
    def to_quadruple(self):
        return "({:.2f}, {:.2f}, {:.2f}, {:.2f})".format(self.a, self.b, self.c, self.d)
    
    @staticmethod
    def main():
        q = Quaternion(1.0, 2.0, 3.0, 4.0)
        q1 = Quaternion(2.0, 3.0, 4.0, 5.0)
        q2 = Quaternion(3.0, 4.0, 5.0, 6.0)
        r = 7.0
        print("q       = " + str(q))
        print("q1      = " + str(q1))
        print("q2      = " + str(q2))
        print("r       = " + str(r))
        print("||q||   = " + str(q.norm()))
        print("-q      = " + str(q.negative()))
        print("q*      = " + str(q.conjugate()))
        print("q + r   = " + str(q.add(r)))
        print("q1 + q2 = " + str(q1.add(q2)))
        print("q * r   = " + str(q.times(r)))
        q1q2 = q1.times(q2)
        q2q1 = q2.times(q1)
        print("q1 * q2 = " + str(q1q2))
        print("q2 * q1 = " + str(q2q1))
        if q1q2 == q2q1:
            print("q1 * q2 = q2 * q1")
        else:
            print("q1 * q2 ≠ q2 * q1")