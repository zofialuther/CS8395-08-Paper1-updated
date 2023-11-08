```python
from tkinter import Tk, Canvas

def dragonCurve(N):
    DCL = dcg_dg(N, ['left'], [], [])
    Side = 4
    Angle = -N * (3.14159/4)
    P = []
    dcg_computePath(Side, Angle, DCL, (180, 400), P, [])
    
    root = Tk()
    canvas = Canvas(root, width=800, height=600)
    canvas.create_line(P, fill="black")
    canvas.pack()
    root.mainloop()

def dcg_computePath(Side, Angle, DCL, point):
    X1, Y1 = point
    P = [(X1, Y1)]
    X2 = X1 + Side * math.cos(Angle)
    Y2 = Y1 + Side * math.sin(Angle)
    Angle1 = Angle + 3.14159 / 2
    P += dcg_computePath(Side, Angle1, DCL, (X2, Y2))
    return P

def dcg_dg(N, L, L1, _):
    if N == 1:
        return L
    else:
        L1 = dcg_dg(L, L1, [])
        N1 = N - 1
        return dcg_dg(N1, L1)

def inverse(L):
    if len(L) == 0:
        return []
    else:
        return inverse(L[1:]) + inverse(L[0])

dragonCurve(10)
```