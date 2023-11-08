```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"Point coordinates: ({self.x}, {self.y})")


class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_radius(self):
        return self.r

    def set_radius(self, r):
        self.r = r

    def print_circle(self):
        print(f"Circle center: ({self.x}, {self.y}), Radius: {self.r}")


if __name__ == "__main__":
    p = Point(3, 4)
    c = Circle(0, 0, 5)
    p.print_point()
    c.print_circle()
```