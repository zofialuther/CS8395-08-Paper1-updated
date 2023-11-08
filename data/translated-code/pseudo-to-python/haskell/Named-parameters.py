X = X
Y = Y

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Point " + str(self.x) + " " + str(self.y)

def createPointAt(X, x, Y, y):
    return Point(x, y)

print(createPointAt(X, 5, Y, 3)