from tkinter import *
import random
import math

def draw_circle(L):
    root = Tk()
    canvas = Canvas(root, width=400, height=400)
    canvas.pack()

    for x, y in L:
        canvas.create_oval(x, y, x+4, y+4, fill="black")

    root.mainloop()

def init():
    BL = [[X, Y] for X in range(-15, 16) for Y in range(-15, 16) if 100 <= X**2 + Y**2 <= 225]
    N = len(BL)
    L = []

    for _ in range(100):
        i = random.randint(0, N-1)
        L.append(BL[i])

    L = [[10*X + 200, 10*Y + 200] for X, Y in L]
    draw_circle(L)

init()