```python
import random
from PIL import Image

def transform1(x, y):
    new_x = 0
    new_y = 0.16 * y
    return new_x, new_y

def transform2(x, y):
    new_x = 0.85 * x + 0.04 * y
    new_y = -0.04 * x + 0.85 * y + 1.6
    return new_x, new_y

def transform3(x, y):
    new_x = 0.2 * x - 0.26 * y
    new_y = 0.23 * x + 0.22 * y + 1.6
    return new_x, new_y

def transform4(x, y):
    new_x = -0.15 * x + 0.28 * y
    new_y = 0.26 * x + 0.24 * y + 0.44
    return new_x, new_y

def apply_transform(x, y):
    r = random.uniform(0, 1)
    if r < 0.01:
        return transform1(x, y)
    elif r < 0.86:
        return transform2(x, y)
    elif r < 0.93:
        return transform3(x, y)
    else:
        return transform4(x, y)

def fern(n):
    x, y = 0, 0
    points = []
    for i in range(n):
        x, y = apply_transform(x, y)
        points.append((x, y))
    return points

def drawFern(points, width, height):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    pixels = img.load()
    for point in points:
        x, y = point
        px = int((x + 3) * (width - 1) / 6)
        py = int((y - 1) * (height - 1) / 10)
        pixels[px, py] = (0, 128, 0)
    img.show()

def main(width, height, num_points):
    points = fern(num_points)
    drawFern(points, width, height)

if __name__ == "__main__":
    import sys
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    num_points = int(sys.argv[3])
    main(width, height, num_points)
```