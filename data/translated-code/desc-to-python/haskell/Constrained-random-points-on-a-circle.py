```python
import random

# create grid of blank spaces
canvas = [[" " for _ in range(10)] for _ in range(10)]

# select and randomize circle points
circle_points = [(x, y) for x in range(10) for y in range(10) if (x-5)**2 + (y-5)**2 <= 25]
random.shuffle(circle_points)

# paint first 100 circle points on canvas
for i in range(min(100, len(circle_points))):
    x, y = circle_points[i]
    canvas[y][x] = "o"

# display canvas with circle points
for row in canvas:
    print(" ".join(row))
```