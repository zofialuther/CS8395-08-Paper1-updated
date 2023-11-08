```python
import tkinter as tk
import math

def draw_tree(canvas, x1, y1, angle, depth):
    if depth == 0:
        return
    else:
        x2 = x1 + math.cos(math.radians(angle)) * depth * 10.0
        y2 = y1 + math.sin(math.radians(angle)) * depth * 10.0
        canvas.create_line(x1, y1, x2, y2)
        a1 = angle - 30
        a2 = angle + 30
        draw_tree(canvas, x2, y2, a1, depth - 1)
        draw_tree(canvas, x2, y2, a2, depth - 1)

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
draw_tree(canvas, 400, 500, -90, 9)
root.mainloop()
```