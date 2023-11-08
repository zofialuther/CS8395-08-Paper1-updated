```python
import random
import math

def pt(x, y, r, g, b):
    return (x, y, r, g, b)

def voronoi():
    V = random.randint(20, 40)
    pt.clear()
    for i in range(1, V+1):
        X = random.randint(5, 395)
        Y = random.randint(5, 395)
        R = random.randint(0, 65535)
        G = random.randint(0, 65535)
        B = random.randint(0, 65535)
        pt(i, X, Y, R, G, B)
    voronoi_func('manhattan', V)
    voronoi_func('euclide', V)
    voronoi_func('minkowski_3', V)

def voronoi_func(distance, V):
    A = f'Voronoi 400X400 {V} {distance}'
    D = Window(A)
    D.size = (400, 400)
    Img = Image(width=400, height=400, kind='pixmap')
    L = [(N, X, Y) for (N, X, Y, R, G, B) in pt]
    for I in range(400):
        for J in range(400):
            S = get_nearest_site(distance, I, J, L)
            (N, X, Y, R, G, B) = pt[S]
            Img.pixel(I, J, color=(R, G, B))
    Bmp = Bitmap(Img)
    D.display(Bmp, point=(0, 0))
    D.open()

def get_nearest_site(distance, I, J, L):
    min_dist = 65535
    min_site = None
    for site in L:
        (N, X, Y) = site
        dist = distance(I, J, X, Y)
        if dist < min_dist:
            min_dist = dist
            min_site = N
    return min_site

def manhattan(X1, Y1, X2, Y2):
    return abs(X2 - X1) + abs(Y2 - Y1)

def euclide(X1, Y1, X2, Y2):
    return math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

def minkowski_3(X1, Y1, X2, Y2):
    return (abs(X2 - X1)**3 + abs(Y2 - Y1)**3)**0.33
```