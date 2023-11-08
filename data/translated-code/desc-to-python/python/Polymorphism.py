```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Circle:
    def __init__(self, center=Point(0, 0), radius=1):
        self.center = center
        self.radius = radius
    
    def __str__(self):
        return f"Center: {self.center}, Radius: {self.radius}"
```