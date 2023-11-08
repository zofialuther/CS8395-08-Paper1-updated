import tkinter as tk
import math

class PendulumAnimation:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        self.length = 150
        self.angle = 0
        self.rod = self.canvas.create_line(300, 50, 300, 200, width=3)
        self.bob = self.canvas.create_oval(295, 195, 305, 205, fill='black')
        self.animate()

    def animate(self):
        self.angle += 0.05
        x = 300 + self.length * math.sin(self.angle)
        y = 50 + self.length * math.cos(self.angle)
        self.canvas.coords(self.rod, 300, 50, x, y)
        self.canvas.coords(self.bob, x-5, y-5, x+5, y+5)
        self.root.after(50, self.animate)

root = tk.Tk()
root.title("Pendulum")
pendulum = PendulumAnimation(root)
root.mainloop()