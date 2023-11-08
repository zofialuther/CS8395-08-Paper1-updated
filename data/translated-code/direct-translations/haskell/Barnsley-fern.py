```python
import random
import argparse
import numpy as np
import matplotlib.pyplot as plt

type Pt = (float, float)

# Four affine transformations used to produce a Barnsley fern.
def f1(p: Pt) -> Pt:
    x, y = p
    return (0, 0.16 * y)

def f2(p: Pt) -> Pt:
    x, y = p
    return (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60)

def f3(p: Pt) -> Pt:
    x, y = p
    return (0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.60)

def f4(p: Pt) -> Pt:
    x, y = p
    return (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)

# Given a random number in [0, 1) transform an initial point by a randomly
# chosen function.
def func(p: Pt, r: float) -> Pt:
    if r < 0.01:
        return f1(p)
    elif r < 0.86:
        return f2(p)
    elif r < 0.93:
        return f3(p)
    else:
        return f4(p)

# Using a sequence of uniformly distributed random numbers in [0, 1) return
# the same number of points in the fern.
def fern(rs: list[float]) -> list[Pt]:
    points = [(0, 0)]
    for r in rs:
        points.append(func(points[-1], r))
    return points

# Given a supply of random values and a count, generate a diagram of a fern
# composed of that number of points.
def drawFern(rs: list[float], n: int) -> None:
    points = fern(rs)
    x, y = zip(*points[:n])
    plt.scatter(x, y, s=1, c='g')
    plt.show()

# To generate a PNG image of a fern, call this program like:
#
#   fern -o fern.png -w 640 -h 640 50000
#
# where the arguments specify the width, height and number of points in the
# image.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_points", type=int, help="Number of points in the image")
    args = parser.parse_args()
    
    random.seed()
    rs = [random.random() for _ in range(args.num_points)]
    drawFern(rs, args.num_points)
```