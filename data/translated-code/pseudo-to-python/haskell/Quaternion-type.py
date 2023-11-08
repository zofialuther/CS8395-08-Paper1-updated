class Quaternion:
    def __init__(self, a, b, c, d):
        self.elements = [a, b, c, d]

def realQ(quaternion):
    return quaternion.elements[0]

def imagQ(quaternion):
    return quaternion.elements[1:]

def quaternionFromScalar(scalar):
    return Quaternion(scalar, 0, 0, 0)

def listFromQ(quaternion):
    return quaternion.elements

def quaternionFromList(lst):
    return Quaternion(*lst)

def normQ(quaternion):
    return sum(x**2 for x in quaternion.elements)**0.5

def conjQ(quaternion):
    return Quaternion(quaternion.elements[0], -quaternion.elements[1], -quaternion.elements[2], -quaternion.elements[3])

def main():
    q = Quaternion(1.0, 2.0, 3.0, 4.0)
    q1 = Quaternion(2.0, 3.0, 4.0, 5.0)
    q2 = Quaternion(3.0, 4.0, 5.0, 6.0)
    print(quaternionFromList([0, 1, 0, 0]).elements * quaternionFromList([0, 0, 1, 0]).elements * quaternionFromList([0, 0, 0, 1]).elements)
    print([a*b for a, b in zip(q1.elements, q2.elements)])
    print([a*b for a, b in zip(q2.elements, q1.elements)])
    print([a*b for a, b in zip(q1.elements, q2.elements)] == [a*b for a, b in zip(q2.elements, q1.elements)])
    print(imagQ(q).elements)