```python
import math

class CirclePoints:
    def __init__(self, segments):
        self.segments = segments

    def unity(self, n):
        angle = 2 * math.pi * n / self.segments
        x = math.cos(angle)
        y = math.sin(angle)
        print(f"({x}, {y})")

    def generate_points(self):
        for i in range(self.segments):
            self.unity(i)

# Example usage
circle = CirclePoints(8)
circle.generate_points()
```