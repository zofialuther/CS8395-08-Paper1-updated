class X:
    def __init__(self):
        pass

class Y:
    def __init__(self):
        pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def createPointAt(x_obj, x, y_obj, y):
    return Point(x, y)

x = X()
y = Y()

print(createPointAt(x, 5, y, 3))