```python
import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot:
    MAX_ITER = 570
    ZOOM = 150
    I = np.zeros((800, 600))

    def __init__(self):
        self.fig = plt.figure()
        self.I = np.zeros((800, 600))
        for x in range(800):
            for y in range(600):
                zx, zy, cX, cY, tmp = 0, 0, 0, 0, 0
                zx, zy = 0, 0
                cX = (x - 400) / self.ZOOM
                cY = (y - 300) / self.ZOOM
                iter = self.MAX_ITER
                while (zx * zx + zy * zy < 4 and iter > 0):
                    tmp = zx * zx - zy * zy + cX
                    zy, zx = 2.0 * zx * zy + cY, tmp
                    iter -= 1
                self.I[x, y] = iter

    def paint(self):
        plt.imshow(self.I, cmap='hot', interpolation='bilinear')
        plt.show()

if __name__ == '__main__':
    mandelbrot = Mandelbrot()
    mandelbrot.paint()
```