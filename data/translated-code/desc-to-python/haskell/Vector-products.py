class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def dot_product(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

def cross_product(a, b):
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x
    return Vector(x, y, z)

def scalar_triple_product(a, b, c):
    return dot_product(a, cross_product(b, c))

def vector_triple_product(a, b, c):
    return cross_product(a, cross_product(b, c))

a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
c = Vector(7, 8, 9)
d = Vector(10, 11, 12)

def main():
    print("Dot product of a and b:", dot_product(a, b))
    print("Cross product of a and b:", cross_product(a, b))
    print("Scalar triple product of a, b, and c:", scalar_triple_product(a, b, c))
    print("Vector triple product of a, b, and c:", vector_triple_product(a, b, c))

main()