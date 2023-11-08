import random
import math

grid = [[' ' for _ in range(31)] for _ in range(31)]
center = (15, 15)

for x in range(31):
    for y in range(31):
        if math.hypot(x - center[0], y - center[1]) <= 15:
            if random.random() > 0.5:
                grid[x][y] = 'X'

for row in grid:
    print(''.join(row))