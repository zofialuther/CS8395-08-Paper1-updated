```python
from tkinter import *
import random

row = 9

class GaltonBox:
    def __init__(self):
        self.tubes = []
        self.balls = []
        self.stop = False
        self.window = Tk()
        self.window.title('Galton Box')
        self.window.geometry('520x700')
        self.display_pins()
        self.display_tubes()
        self.window.protocol("WM_DELETE_WINDOW", self.destroy_window)
        self.window.mainloop()

    def display_pins(self):
        for i in range(row + 1):
            start = 250 - i * 20
            y = i * 30 + 50
            for j in range(i + 1):
                x = start + j * 40
                self.create_pin(x, y)

    def display_tubes(self):
        for i in range(row + 2):
            self.create_tube(i)

    def create_pin(self, x, y):
        pin = Canvas(self.window, width=18, height=18, bg='black', highlightthickness=0)
        pin.create_oval(0, 0, 18, 18, fill='black')
        pin.place(x=x, y=y)

    def create_tube(self, i):
        x0 = 228 - row * 20 + i * 40
        x1 = x0 + 20
        y0, y1 = 350, 600
        tube = Canvas(self.window, width=20, height=250, bg='white', highlightthickness=0)
        tube.create_rectangle(x0, y0, x1, y1, fill='white')
        tube.pack()

    def destroy_window(self):
        self.clear_tubes()
        self.clear_balls()
        self.window.destroy()

    def clear_tubes(self):
        for tube in self.tubes:
            tube.pack_forget()
        self.tubes = []

    def clear_balls(self):
        for ball in self.balls:
            ball.pack_forget()
        self.balls = []

    def next_ball(self):
        self.create_ball()
    
    def create_ball(self):
        ball = Canvas(self.window, width=18, height=18, bg='red', highlightthickness=0)
        ball.create_oval(0, 0, 18, 18, fill='red')
        ball.place(x=250, y=30)
        self.balls.append(ball)
        self.animate_ball(ball)

    def animate_ball(self, ball):
        ball.move(0, 4)
        if ball.winfo_y() < 600:
            self.window.after(5, lambda: self.animate_ball(ball))
        else:
            self.check_stop(ball)

    def check_stop(self, ball):
        if len(self.tubes[ball.winfo_x() // 40].balls) < 12:
            self.tubes[ball.winfo_x() // 40].add_ball()
            self.check_stop_tube()

    def check_stop_tube(self):
        for tube in self.tubes:
            if len(tube.balls) == 12:
                self.stop = True
                break

    def create_tube(self, i):
        tube = Canvas(self.window, width=20, height=250, bg='white', highlightthickness=0)
        x0 = 228 - row * 20 + i * 40
        x1 = x0 + 20
        y0, y1 = 350, 600
        tube.create_rectangle(x0, y0, x1, y1, fill='white')
        tube.balls = []
        tube.pack()
        self.tubes.append(tube)

    def add_ball(self):
        self.balls += 1
        if len(self.balls) < 12:
            self.stop = True

GaltonBox()
```