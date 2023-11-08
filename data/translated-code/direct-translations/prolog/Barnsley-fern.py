```python
import random

def replicate(term, times):
    return [term] * times

def replace(x, lst, e):
    lst[x] = e
    return lst

def replace_2d(x, y, lst, e):
    lst[y][x] = e
    return lst

def fern_iteration(n, x, y, i):
    final = i
    if n == 10000:
        return final
    else:
        r = random.random()
        if r <= 0.01:
            x1 = 0.0
            y1 = 0.16 * y
        elif r <= 0.86:
            x1 = 0.85 * x + 0.04 * y
            y1 = -0.04 * x + 0.85 * y + 1.6
        elif r <= 0.93:
            x1 = 0.20 * x - 0.26 * y
            y1 = 0.23 * x + 0.22 * y + 1.60
        else:
            x1 = -0.15 * x + 0.28 * y
            y1 = 0.26 * x + 0.24 * y + 0.44
        point_x = 250 + int(70.0 * x1)
        point_y = 750 - int(70.0 * y1)
        i = replace_2d(point_x, point_y, i, [0, 255, 0])
        n += 1
        return fern_iteration(n, x1, y1, i)

def draw_fern():
    row = replicate([0, 0, 0], 750)
    f = replicate(row, 500)
    fern = fern_iteration(0, 0, 0, f)
    with open('fern.ppm', 'wb') as file:
        flat_fern = [item for sublist in fern for item in sublist]
        file.write(bytearray(f"P6\n500 750\n255\n", 'utf-8'))
        file.write(bytearray(flat_fern))

draw_fern()
```