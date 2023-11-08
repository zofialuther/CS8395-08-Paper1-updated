```python
import random

def voronoi():
    V = random.randint(20, 40)
    pt = []
    for I in range(1, V+1):
        X = random.randint(5, 395)
        Y = random.randint(5, 395)
        R = random.randint(0, 65535)
        G = random.randint(0, 65535)
        B = random.randint(0, 65535)
        pt.append((I, X, Y, R, G, B))

    voronoi_method("manhattan", V, pt)
    voronoi_method("euclide", V, pt)
    voronoi_method("minkowski_3", V, pt)

def voronoi_method(Distance, V, pt):
    L = pt
    for I in range(400):
        for J in range(400):
            S = get_nearest_site(Distance, I, J, L)
            R, G, B = pt[S-1][3], pt[S-1][4], pt[S-1][5]
            # Displaying pixel with color R, G, B at coordinates (I, J)

def foldl(L, Pred, Acc, R):
    if not L:
        return R
    else:
        H = L[0]
        T = L[1:]
        R1 = Pred(H, Acc)
        return foldl(T, Pred, R1, R)

def compare(Distance, XP, YP, site, current):
    (N, X, Y) = site
    (D, S) = current
    DT = Distance(XP, YP, X, Y)
    if DT < D:
        return (DT, N)
    else:
        return (D, S)

def get_nearest_site(Distance, I, J, L):
    return foldl(L, lambda site, current: compare(Distance, I, J, site, current), (65535, None), (0, None))

def manhattan(X1, Y1, X2, Y2):
    return abs(X2 - X1) + abs(Y2 - Y1)

def euclide(X1, Y1, X2, Y2):
    return ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5

def minkowski_3(X1, Y1, X2, Y2):
    return ((abs(X2 - X1)**3 + abs(Y2 - Y1)**3)**(1/3))
```