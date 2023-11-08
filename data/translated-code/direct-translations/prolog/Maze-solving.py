```python
from tkinter import *
import random

def maze_solve(Lig,Col):
    # add maze, cell, and path as dynamic variables
    cell = {}
    maze = {}
    path = []

    # initialisation of the neighbours of the cells
    for I in range(Lig+1):
        for J in range(Col+1):
            maze[(I, J)] = []

    # create the window of the maze
    window = Tk()
    canvas = Canvas(window, width=Col*30+100, height=Lig*30+100)
    canvas.pack()

    for I in range(Lig+1):
        XL = 50
        YL = I * 30 + 50
        XR = Col * 30 + 50
        canvas.create_line(XL, YL, XR, YL)

    for I in range(Col+1):
        XT = 50 + I * 30
        YT = 50
        YB = Lig * 30 + 50
        canvas.create_line(XT, YT, XT, YB)

    L0 = random.randint(0, Lig)
    C0 = random.randint(0, Col)
    cell[(L0, C0)] = True

    # look for a path from cell(0, 0) to cell(Lig-1, Col-1)
    # creation of the entrance
    canvas.create_line(50, 50, 50, 50)

    # creation of the exit
    canvas.create_line(Col * 30 + 50, Lig * 30 + 50, Col * 30 + 50, Lig * 30 + 50)

    # search the path
    path.append((0, 0))
    walk(Lig, Col)

    display_path(canvas, path)

def walk(Lig, Col):
    global path
    if path[0] == (Lig-1, Col-1):
        return
    else:
        L, C = path.pop(0)
        path.insert(0, (Lig, C))

def display_path(canvas, path):
    for node in path:
        X = node[1] * 30 + 60
        Y = node[0] * 30 + 60
        canvas.create_rectangle(X-5, Y-5, X+5, Y+5, fill="black")

maze_solve(10, 10)
```