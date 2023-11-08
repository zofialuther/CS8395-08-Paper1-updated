```python
import math
import tkinter as tk

class FractalTree(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Fractal Tree")
        self.geometry("800x600")
        self.resizable(False, False)

    def draw_tree(self, canvas, x1, y1, angle, depth):
        if depth == 0:
            return
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        canvas.create_line(x1, y1, x2, y2)
        self.draw_tree(canvas, x2, y2, angle - 20, depth - 1)
        self.draw_tree(canvas, x2, y2, angle + 20, depth - 1)

    def draw_fractal_tree(self):
        canvas = tk.Canvas(self, width=800, height=600, bg="white")
        canvas.pack()
        self.draw_tree(canvas, 400, 500, -90, 9)

    def run(self):
        self.draw_fractal_tree()
        self.mainloop()

if __name__ == "__main__":
    fractal_tree = FractalTree()
    fractal_tree.run()
```