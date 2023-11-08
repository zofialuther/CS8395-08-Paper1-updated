```python
from tkinter import *
import math

class PendulumAnimation:
    def __init__(self, window, length, angle, angular_velocity):
        self.window = window
        self.length = length
        self.angle = angle
        self.angular_velocity = angular_velocity
        self.line = None
        self.bob = None
        self.timer = None
        self.draw_pendulum()

    def draw_pendulum(self):
        self.line = self.window.create_line(200, 100, 200 + self.length * math.sin(self.angle), 100 + self.length * math.cos(self.angle), width=2)
        self.bob = self.window.create_oval(0, 0, 0, 0, width=2, fill='blue')
        self.update_bob_position()

    def update_bob_position(self):
        x = 200 + self.length * math.sin(self.angle)
        y = 100 + self.length * math.cos(self.angle)
        self.window.coords(self.bob, x - 10, y - 10, x + 10, y + 10)

    def update_angle(self):
        self.angle += self.angular_velocity
        self.update_bob_position()

    def start_animation(self):
        self.timer = self.window.after(50, self.update_animation)

    def stop_animation(self):
        if self.timer:
            self.window.after_cancel(self.timer)

    def update_animation(self):
        self.update_angle()
        self.timer = self.window.after(50, self.update_animation)

window = Tk()
window.geometry("400x200")
canvas = Canvas(window, width=400, height=200)
canvas.pack()

animation = PendulumAnimation(canvas, 100, math.pi/4, 0.1)
animation.start_animation()

window.mainloop()
```