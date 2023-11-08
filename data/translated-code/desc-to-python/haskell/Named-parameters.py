class X:
    pass

class Y:
    pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def createPointAt(x, integer_x, y, integer_y):
    return Point(integer_x, integer_y)

def main():
    p = createPointAt(X, 5, Y, 3)
    print((p.x, p.y))

main()