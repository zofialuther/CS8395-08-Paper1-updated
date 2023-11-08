```python
import collections
import random

# Create a default dictionary
world = collections.defaultdict(int)

# List of points
points = [1, 2, 3, 4, 5]

# Populate world dictionary with randomly selected points
for _ in range(10):
    point = random.choice(points)
    world[point] += 1

# Print out a visual representation of the populated world
for point, count in world.items():
    print(str(point) + ': ' + '*' * count)
```