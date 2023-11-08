```python
import math
from graphics import *

def dragonCurve(N):
    dcg_dg(N, ['left'], [], [])
    Side = 4
    Angle = -N * (math.pi/4)
    P = []
    dcg_computePath(Side, Angle, [], Point(180, 400), P, [])
    D = GraphWin('Dragon Curve', 800, 600)
    Path = Polygon(P)
    Path.draw(D)
    D.mainloop()

def dcg_computePath(Side, Angle, DCT, point):
    X1, Y1 = point.getX(), point.getY()
    X2 = X1 + Side * math.cos(Angle)
    Y2 = Y1 + Side * math.sin(Angle)
    Angle1 = Angle + math.pi / 2 if 'left' in DCT else Angle - math.pi / 2
    if DCT:
        dcg_computePath(Side, Angle1, DCT[1:], Point(X2, Y2))

def dcg_dg(N, L, L1, L2):
    if N == 1:
        return L
    else:
        dcg_dg(L, L1, [])
        N1 = N - 1
        return dcg_dg(N1, L1, [])

def inverse(T):
    if T:
        inverse(T[1:])
        if T[0] == 'left':
            return 'right'
        else:
            return 'left'
    else:
        return []

```