class Circle:
    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y
        self.r = r

    def copy(self):
        return Circle(self.x, self.y, self.r)

    def print(self):
        print("Circle (" + str(self.x) + ", " + str(self.y) + ", " + str(self.r) + ")")

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    def print(self):
        print("Point (" + str(self.x) + ", " + str(self.y) + ")")

def main():
    p1 = Point()
    p2 = Point(1)
    p3 = Point(1, 2)
    p4 = p3.copy()

    print("Points:")
    p1.print()
    p2.print()
    p3.print()
    p4.print()
    # demonstrate field mutator/accessor
    p3.x = 3
    print("p3 value of x is: " + str(p3.x))

    c1 = Circle()
    c2 = Circle(1)
    c3 = Circle(1, 2)
    c4 = Circle(1, 2, 3)

    print("Circles:")
    c1.print()
    c2.print()
    c3.print()
    c4.print()

main()