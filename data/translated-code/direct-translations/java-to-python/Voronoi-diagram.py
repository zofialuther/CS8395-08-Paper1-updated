```python
import random
import math
from PIL import Image, ImageDraw

class Voronoi:
    def __init__(self):
        self.p = 3
        self.cells = 100
        self.size = 1000
        self.I = Image.new("RGB", (self.size, self.size), "white")
        self.px = [random.randint(0, self.size) for _ in range(self.cells)]
        self.py = [random.randint(0, self.size) for _ in range(self.cells)]
        self.color = [random.randint(0, 16777215) for _ in range(self.cells)]
        
        for x in range(self.size):
            for y in range(self.size):
                n = 0
                for i in range(self.cells):
                    if self.distance(self.px[i], x, self.py[i], y) < self.distance(self.px[n], x, self.py[n], y):
                        n = i
                self.I.putpixel((x, y), self.color[n])
                
        draw = ImageDraw.Draw(self.I)
        for i in range(self.cells):
            draw.ellipse((self.px[i] - 2.5, self.py[i] - 2.5, self.px[i] + 2.5, self.py[i] + 2.5), fill="black")
            
        self.I.save("voronoi.png", "PNG")
        
    def distance(self, x1, x2, y1, y2):
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Euclidian
        # d = abs(x1 - x2) + abs(y1 - y2)  # Manhattan
        # d = (abs(x1 - x2) ** self.p + abs(y1 - y2) ** self.p) ** (1 / self.p)  # Minkovski
        return d

voronoi = Voronoi()
```