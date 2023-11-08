```python
from tkinter import *
import math
import random

class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Dining philosophers")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)

        ellipse = canvas.create_oval(320, 320, 480, 480)

        forks = []
        for i in range(5):
            fork = Fork(canvas, i)
            forks.append(fork)

        waiter = Waiter(forks[0], forks[1], forks[2], forks[3], forks[4])

        plates = []
        for i in range(5):
            plate = Plate(canvas, i)
            plates.append(plate)

        philosophers = []
        for i, name in enumerate(['Aristotle', 'Kant', 'Spinoza', 'Marx', 'Russell']):
            philosopher = Philosopher(name, waiter, plates[i], canvas, i)
            philosophers.append(philosopher)

        waiter.init_phi(philosophers[0], philosophers[1], philosophers[2], philosophers[3], philosophers[4])

        for philosopher in philosophers:
            philosopher.start()

        canvas.create_text(400, 760, text="Statistics", font=("Arial", 16))

class Fork:
    def __init__(self, canvas, number):
        self.canvas = canvas
        self.number = number
        self.status = "free"
        self.side = None
        self.value = number
        self.draw()

    def draw(self):
        angle = self.number * math.pi / 2.5 + math.pi / 5
        xs = 400 + 100 * math.cos(angle)
        ys = 400 + 100 * math.sin(angle)
        xe = 400 + 180 * math.cos(angle)
        ye = 400 + 180 * math.sin(angle)
        self.line = self.canvas.create_line(xs, ys, xe, ye)

    def free(self):
        self.status = "free"
        self.position()

    def used(self, side):
        self.status = "used"
        self.side = side
        self.position()

    def position(self):
        angle = self.value * math.pi / 2.5 + math.pi / 5
        if self.status == "free":
            start_x = 400 + 100 * math.cos(angle)
            start_y = 400 + 100 * math.sin(angle)
            end_x = 400 + 180 * math.cos(angle)
            end_y = 400 + 180 * math.sin(angle)
        elif self.side == "left":
            angle -= 2 * math.pi / 15
            start_x = 400 + 100 * math.cos(angle)
            start_y = 400 + 100 * math.sin(angle)
            end_x = 400 + 180 * math.cos(angle)
            end_y = 400 + 180 * math.sin(angle)
        elif self.side == "right":
            angle += 2 * math.pi / 15
            start_x = 400 + 100 * math.cos(angle)
            start_y = 400 + 100 * math.sin(angle)
            end_x = 400 + 180 * math.cos(angle)
            end_y = 400 + 180 * math.sin(angle)
        self.canvas.coords(self.line, start_x, start_y, end_x, end_y)

class Waiter:
    def __init__(self, f1, f2, f3, f4, f5):
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.f4 = f4
        self.f5 = f5
        self.phi1 = None
        self.phi2 = None
        self.phi3 = None
        self.phi4 = None
        self.phi5 = None

    def init_phi(self, phi1, phi2, phi3, phi4, phi5):
        self.phi1 = phi1
        self.phi2 = phi2
        self.phi3 = phi3
        self.phi4 = phi4
        self.phi5 = phi5

    def want_forks(self, phi):
        if phi == self.phi1 and self.f5.status == "free" and self.f1.status == "free":
            self.check_forks(phi, self.f5, self.f1)
        elif phi == self.phi2 and self.f1.status == "free" and self.f2.status == "free":
            self.check_forks(phi, self.f1, self.f2)
        elif phi == self.phi3 and self.f2.status == "free" and self.f3.status == "free":
            self.check_forks(phi, self.f2, self.f3)
        elif phi == self.phi4 and self.f3.status == "free" and self.f4.status == "free":
            self.check_forks(phi, self.f3, self.f4)
        elif phi == self.phi5 and self.f4.status == "free" and self.f5.status == "free":
            self.check_forks(phi, self.f4, self.f5)

    def give_back_forks(self, phi):
        if phi == self.phi1:
            self.release_forks(phi)
            self.check_forks(self.phi1, self.f5, self.f1)
            self.check_forks(self.phi2, self.f1, self.f2)
            self.check_forks(self.phi3, self.f2, self.f3)
            self.check_forks(self.phi4, self.f3, self.f4)
            self.check_forks(self.phi5, self.f4, self.f5)
        elif phi == self.phi2:
            self.release_forks(phi)
            self.check_forks(self.phi2, self.f1, self.f2)
            self.check_forks(self.phi3, self.f2, self.f3)
            self.check_forks(self.phi4, self.f3, self.f4)
            self.check_forks(self.phi5, self.f4, self.f5)
        elif phi == self.phi3:
            self.release_forks(phi)
            self.check_forks(self.phi3, self.f2, self.f3)
            self.check_forks(self.phi4, self.f3, self.f4)
            self.check_forks(self.phi5, self.f4, self.f5)
        elif phi == self.phi4:
            self.release_forks(phi)
            self.check_forks(self.phi4, self.f3, self.f4)
            self.check_forks(self.phi5, self.f4, self.f5)
        elif phi == self.phi5:
            self.release_forks(phi)
            self.check_forks(self.phi5, self.f4, self.f5)

    def release_forks(self, phi):
        if phi == self.phi1:
            self.f5.free()
            self.f1.free()
        elif phi == self.phi2:
            self.f1.free()
            self.f2.free()
        elif phi == self.phi3:
            self.f2.free()
            self.f3.free()
        elif phi == self.phi4:
            self.f3.free()
            self.f4.free()
        elif phi == self.phi5:
            self.f4.free()
            self.f5.free()

    def check_forks(self, phi, f1, f2):
        if phi.status == "waiting" and f1.status == "free" and f2.status == "free":
            phi.receive_forks()
            f1.used("right")
            f2.used("left")

class Philosopher:
    def __init__(self, name, waiter, plate, canvas, number):
        self.name = name
        self.waiter = waiter
        self.plate = plate
        self.canvas = canvas
        self.number = number
        self.status = "thinking"
        self.window_stat = None
        self.line_stat = None
        self.point = None
        self.side = "left"
        self.old_text = None
        self.stat_wait = None
        self.stat_eat = None
        self.stat_think = None

    def unlink(self):
        if self.status == "eating":
            self.stat_eat.stop()
        elif self.status == "waiting":
            self.stat_wait.stop()
        elif self.status == "thinking":
            self.stat_think.stop()
        self.display_statistics()

    def initialise(self):
        self.line_stat = self.number * 5
        self.waiter = Waiter
        self.plate = Plate
        self.status = "thinking"
        self.window_stat = Window
        self.point = Point
        self.side = "left"
        self.old_text = Text(" ")
        self.display_status()
        self.stat_wait = MyStat("Waiting")
        self.stat_eat = MyStat("Eating")
        self.stat_think = MyStat("Thinking")

    def display_statistics(self):
        self.window_stat.create_text(30, self.line_stat * 30, text=f"Statistics of philosopher: {self.name}", font=("Arial", 16))
        self.stat_wait.statistics(self.window_stat, self.line_stat + 1)
        self.stat_eat.statistics(self.window_stat, self.line_stat + 2)
        self.stat_think.statistics(self.window_stat, self.line_stat + 3)

    def stop_timer(self):
        if self.status == "eating":
            self.stat_eat.stop()
        elif self.status == "waiting":
            self.stat_wait.stop()
        elif self.status == "thinking":
            self.stat_think.stop()

    def my_message(self):
        if self.status == "eating":
            self.next_status()
        elif self.status == "thinking":
            self.status = "waiting"
            self.display_status()
            self.stat_think.stop()
            self.waiter.want_forks(self)

    def next_status(self):
        if self.status == "eating":
            self.stat_eat.stop()
            self.stat_think.start()
            self.waiter.give_back_forks(self)
            self.status = "thinking"
            self.display_status()
            self.plate.change_color("white")
            i = random.randint(10, 30)
            self.mytimer = Timer(i, self.my_message)
            self.mytimer.start()

    def receive_forks(self):
        self.stat_wait.stop()
        self.stat_eat.start()
        self.status = "eating"
        self.display_status()
        self.plate.change_color("black")
        i = random.randint(5, 25)
        self.mytimer = Timer(i, self.my_message)
        self.mytimer.start()

    def display_status(self):
        self.old_text.destroy()
        color = self.choose_color()
        text = f"{self.name} {self.status}"
        text = Text(text)
        text.font("Arial 16")
        text.color(color)
        text.place(400, 400)

    def start(self):
        i = random.randint(2, 12)
        self.stat_think.start()
        self.mytimer = Timer(i, self.my_message)
        self.mytimer.start()

    def choose_color(self):
        if self.status == "eating":
            return "blue"
        elif self.status == "thinking":
            return "green"
        elif self.status == "waiting":
            return "red"

class Plate:
    def __init__(self, canvas, number):
        self.canvas = canvas
        self.number = number
        self.create_plate()

    def create_plate(self):
        x = 400 + 140 * math.cos(self.number * math.pi / 2.5)
        y = 400 + 140 * math.sin(self.number * math.pi / 2.5)
        self.plate = canvas.create_oval(x-40, y-40, x+40, y+40)

    def change_color(self, color):
        self.canvas.itemconfig(self.plate, fill=color)

class MyStat:
    def __init__(self, name):
        self.name = name
        self.nb = 0
        self.duration = 0.0
        self.start = 0.0

    def start(self):
        self.start = time.time()

    def stop(self):
        self.duration += time.time() - self.start
        self.nb += 1

    def statistics(self, window, line):
        text = f"{self.name}\n nb: {self.nb} duration: {self.duration}"
        text = Text(text)
        text.font("Arial 14")
        text.place(40, line * 30)

root = Tk()
app = Window(root)
root.mainloop()
```