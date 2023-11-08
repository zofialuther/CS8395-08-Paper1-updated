import math
import time
import threading
import tkinter as tk

class Pendulum(tk.Canvas, threading.Thread):
    def __init__(self, length):
        super().__init__()
        self.angle = math.pi / 2
        self.length = length
        self.pack()
        self.create_oval(0, 0, 0, 0, fill="white")
        self.create_line(0, 0, 0, 0, fill="black")
        self.create_oval(0, 0, 0, 0, fill="black")

    def run(self):
        angle_velocity = 0
        dt = 0.1
        while True:
            angle_accel = -9.81 / self.length * math.sin(self.angle)
            angle_velocity += angle_accel * dt
            self.angle += angle_velocity * dt
            self.update()
            time.sleep(0.015)

def main():
    root = tk.Tk()
    root.title("Pendulum")
    pendulum = Pendulum(200)
    pendulum.start()
    root.mainloop()

if __name__ == "__main__":
    main()