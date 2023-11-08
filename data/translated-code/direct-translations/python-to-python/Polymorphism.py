class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point 0x{id(self):x} x: {self.x} y: {self.y}>'


class Circle:
    def __init__(self, center=None, radius=1.0):
        self.center = center or Point()
        self.radius = radius

    def __repr__(self):
        return f'<Circle 0x{id(self):x} x: {self.center.x} y: {self.center.y} radius: {self.radius}>'