class Quaternion:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def from_scalar(self, scalar):
        return Quaternion(scalar, [0, 0, 0])

    def from_list(self, lst):
        return Quaternion(lst[0], lst[1:])

    def get_real_part(self):
        return self.real

    def get_imag_part(self):
        return self.imag

    def norm(self):
        return (self.real ** 2 + sum([x ** 2 for x in self.imag])) ** 0.5

    def conjugate(self):
        return Quaternion(self.real, [-x for x in self.imag])

    def __add__(self, other):
        return Quaternion(self.real + other.real, [self.imag[i] + other.imag[i] for i in range(len(self.imag))])

    def __sub__(self, other):
        return Quaternion(self.real - other.real, [self.imag[i] - other.imag[i] for i in range(len(self.imag))])

    def __mul__(self, other):
        real = self.real * other.real - sum([self.imag[i] * other.imag[i] for i in range(len(self.imag))])
        imag = [self.real * x for x in other.imag] + [other.real * x for x in self.imag] + [self.imag[1] * other.imag[2] - self.imag[2] * other.imag[1], self.imag[2] * other.imag[0] - self.imag[0] * other.imag[2], self.imag[0] * other.imag[1] - self.imag[1] * other.imag[0]]
        return Quaternion(real, imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

def main():
    q1 = Quaternion(1, [2, 3, 4])
    q2 = Quaternion.from_scalar(2)
    q3 = Quaternion.from_list([3, 4, 5, 6])
    print(q1.get_real_part())
    print(q1.get_imag_part())
    print(q1.norm())
    print(q1.conjugate())
    print(q1 + q2)
    print(q1 - q2)
    print(q1 * q2)
    print(q1 == q2)

main()