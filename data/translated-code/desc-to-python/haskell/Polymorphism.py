class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def copy(self):
        return Point(self.x, self.y)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
    def __repr__(self):
        return f'Circle({self.center}, {self.radius})'
    
    def copy(self):
        return Circle(self.center.copy(), self.radius)

# Main procedure
p1 = Point(3, 4)
p2 = p1.copy()
print(p1)
print(p2)

c1 = Circle(p1, 5)
c2 = c1.copy()
print(c1)
print(c2)

c1.center.x = 10
print(c1)
print(c2)