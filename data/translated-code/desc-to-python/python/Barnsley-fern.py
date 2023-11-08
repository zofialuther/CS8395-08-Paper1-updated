```python
from PIL import Image

class BarnsleyFern:
    def __init__(self, width, height, paint_color, background_color):
        self.width = width
        self.height = height
        self.paint_color = paint_color
        self.background_color = background_color
        self.image = Image.new("RGB", (self.width, self.height), self.background_color)

    def scale(self, point, scale_factor):
        return (point[0] * scale_factor, point[1] * scale_factor)

    def transform(self, point, matrix):
        x = point[0] * matrix[0][0] + point[1] * matrix[0][1] + matrix[0][2]
        y = point[0] * matrix[1][0] + point[1] * matrix[1][1] + matrix[1][2]
        return (x, y)

    def iterate(self, point):
        probability = random.random()
        if probability < 0.01:
            return self.transform(point, [[0, 0], [0, 0.16], [0, 0]])
        elif probability < 0.86:
            return self.transform(point, [[0.85, 0.04], [-0.04, 0.85], [0, 1.60]])
        elif probability < 0.93:
            return self.transform(point, [[0.20, -0.26], [0.23, 0.22], [0, 1.60]])
        else:
            return self.transform(point, [[-0.15, 0.28], [0.26, 0.24], [0, 0.44]])

    def create_fractal(self, iterations):
        point = (0, 0)
        for _ in range(iterations):
            point = self.iterate(point)
            x = int(self.width / 2 + point[0] * self.width / 11)
            y = int(self.height - point[1] * self.height / 11)
            self.image.putpixel((x, y), self.paint_color)

    def display_fractal(self):
        self.image.show()

fern = BarnsleyFern(800, 600, (0, 255, 0), (255, 255, 255))
fern.create_fractal(100000)
fern.display_fractal()
```