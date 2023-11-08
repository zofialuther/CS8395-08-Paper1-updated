```python
import random
import numpy as np
import matplotlib.pyplot as plt

def sqDistance(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

def centers(nCenters, nCells):
    return np.random.rand(nCenters, 2)

def applyReduce2(arr, f):
    return np.apply_along_axis(f, axis=1, arr=arr)

def minimize1D(arr):
    return np.min(arr)

def voronoi(nCenters, nCells):
    centers = generate_centers(nCenters, nCells)
    # implement voronoi diagram algorithm using the centers and cells
    return voronoi_diagram

def genColorTable(n):
    return np.random.rand(n, 3)

def colorize(ctable, arr):
    # implement colorize function to map the color table to the input array
    return colorized_array

def main():
    nsites = 150
    ctable = genColorTable(10)
    voronoi_diagram = voronoi(nsites, 100)
    colorized_diagram = colorize(ctable, voronoi_diagram)
    plt.imshow(colorized_diagram)
    plt.show()
```