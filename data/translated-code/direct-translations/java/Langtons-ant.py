```python
import numpy as np
import matplotlib.pyplot as plt

def run_ant(height, width):
    plane = np.zeros((height, width), dtype=bool)
    ant_x, ant_y = width//2, height//2  # start in the middle-ish
    x_change, y_change = 0, -1  # start moving up
    while 0 <= ant_x < width and 0 <= ant_y < height:
        if plane[ant_y, ant_x]:
            # turn left
            x_change, y_change = y_change, -x_change
        else:
            # turn right
            x_change, y_change = -y_change, x_change
        plane[ant_y, ant_x] = not plane[ant_y, ant_x]
        ant_x += x_change
        ant_y += y_change
    return plane

def plot_langton(plane):
    plt.imshow(plane, cmap='Greys', interpolation='nearest')
    plt.show()

plane = run_ant(100, 100)
plot_langton(plane)
```