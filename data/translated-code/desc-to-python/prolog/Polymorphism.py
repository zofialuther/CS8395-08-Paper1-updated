class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def print_shape(self):
        print(f"Point at ({self.x}, {self.y})")

class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def print_shape(self):
        print(f"Circle at ({self.center.x}, {self.center.y}) with radius {self.radius}")

def default_value():
    return 0

# Tests
point1 = Point(3, 4)
point1.print_shape()
point1.set_coordinates(5, 6)
print(point1.get_coordinates())

circle1 = Circle(2, 3, 5)
circle1.print_shape()
circle1.set_radius(8)
print(circle1.get_radius())