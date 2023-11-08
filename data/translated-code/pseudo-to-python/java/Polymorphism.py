class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def print(self):
        print("Point x:", self.x, "y:", self.y)


class Circle(Point):
    def __init__(self, x=0, y=0, r=0):
        super().__init__(x, y)
        self.r = r

    def getR(self):
        return self.r

    def setR(self, r):
        self.r = r

    def print(self):
        print("Circle x:", self.x, "y:", self.y, "r:", self.r)


def main():
    p = Point()
    c = Circle()
    p.print()
    c.print()


if __name__ == "__main__":
    main()