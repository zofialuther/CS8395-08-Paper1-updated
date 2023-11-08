```python
import functools

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def step(start, step, num_steps):
    return [start + i*step for i in range(num_steps)]

grid = []
for real in step(-2, 0.05, 40):
    row = []
    for imag in step(-2, 0.1, 20):
        c = complex(real, imag)
        val = mandelbrot(c, 30)
        row.append(' ' if val == 30 else '*')
    grid.append(row)

for row in grid:
    print(''.join(row))
```