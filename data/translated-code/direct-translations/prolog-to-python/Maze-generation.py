```python
import random
import tkinter as tk

def maze(Lig, Col):
    global cell
    cell = set()
    
    def erase_line(D, L, C, L1, C1):
        nonlocal canvas
        if C < C1:
            C2 = C1
        else:
            C2 = C
        if L == L1:
            XT = C2 * 30 + 50
            YT = L * 30 + 51
            YR = (L + 1) * 30 + 50
            canvas.create_line(XT, YT, XT, YR, fill="white")
        else:
            XT = 51 + C * 30
            XR = 50 + (C + 1) * 30
            if L < L1:
                L2 = L1
            else:
                L2 = L
            YT = L2 * 30 + 50
            canvas.create_line(XT, YT, XR, YT, fill="white")

    def nextcell(Dir, Lig, Col, L, C):
        if Dir == 0 and L > 0 and (L - 1, C) not in cell:
            return L - 1, C
        elif Dir == 1 and C < Col - 1 and (L, C + 1) not in cell:
            return L, C + 1
        elif Dir == 2 and L < Lig - 1 and (L + 1, C) not in cell:
            return L + 1, C
        elif Dir == 3 and C > 0 and (L, C - 1) not in cell:
            return L, C - 1
        return None, None

    def search(L, C):
        nonlocal canvas, Lig, Col
        Dir = random.randint(0, 3)
        N = nextcell(Dir, Lig, Col, L, C)
        if N != (None, None):
            L1, C1 = N
            cell.add((L1, C1))
            erase_line(D, L, C, L1, C1)
            search(L1, C1)
    
    root = tk.Tk()
    canvas = tk.Canvas(root, width=Col * 30 + 100, height=Lig * 30 + 100)
    canvas.pack()

    for i in range(Lig + 1):
        canvas.create_line(50, i * 30 + 50, Col * 30 + 50, i * 30 + 50)

    for i in range(Col + 1):
        canvas.create_line(50 + i * 30, 50, 50 + i * 30, Lig * 30 + 50)

    L0 = random.randint(0, Lig - 1)
    C0 = random.randint(0, Col - 1)
    cell.add((L0, C0))
    search(L0, C0)
    
    root.mainloop()

maze(10, 10)
```