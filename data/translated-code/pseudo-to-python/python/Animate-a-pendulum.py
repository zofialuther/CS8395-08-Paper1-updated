import tkinter
import math

class Animation:
    def __init__(self, gw):
        self.position = (200, 50)
        self.angle = math.pi / 4
        self.window = gw
        self.canvas = tkinter.Canvas(self.window)
        self.canvas.pack()
        self.line = self.canvas.create_line(self.position[0], self.position[1], 200, 200)
        self.oval = self.canvas.create_oval(190, 190, 210, 210, fill="black")
        self.animate()

    def animate(self):
        if abs(self.angle) > math.pi / 2:
            self.angle *= -1
        self.angle += 0.01
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)
        x = 100 * sin + 200
        y = 100 * cos + 200
        self.canvas.coords(self.line, self.position[0], self.position[1], x, y)
        self.canvas.coords(self.oval, x-10, y-10, x+10, y+10)
        self.window.after(50, self.animate)

root = tkinter.Tk()
root.title("Pendulum Animation")
root.geometry("400x400")
root.resizable(False, False)
anim = Animation(root)
root.mainloop()