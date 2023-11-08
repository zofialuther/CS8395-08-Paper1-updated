from tkinter import *

class Animation:
    def __init__(self, window, angle, boule, len_pendulum):
        self.window = window
        self.angle = angle
        self.boule = boule
        self.len_pendulum = len_pendulum
        self.delta = 0.01
        self.mytimer = Timer(0.01, self.anim_message)

    def initialise(self, W, A, B, L):
        self.window = W
        self.angle = A
        self.boule = B
        self.len_pendulum = L
        self.mytimer = Timer(0.01, self.anim_message)

    def unlink(self):
        self.mytimer.stop()

    def anim_message(self):
        A = self.angle
        L = self.len_pendulum
        X, Y = self.calc(A, L)
        W = self.window
        B = self.boule
        W.display(B, point(X, Y))
        D = self.delta
        NA, ND = self.next_Angle(A, D)
        self.angle = NA
        self.delta = ND

    def calc(self, Ang, Len):
        X = Len * cos(Ang) + 250
        Y = Len * sin(Ang) + 20
        return X, Y

    def next_Angle(self, A, D):
        NA = D + A
        if (D > 0 and abs(pi - NA) < 0.01) or (D < 0 and abs(NA) < 0.01):
            ND = -D
        else:
            ND = D
        return NA, ND


pendulum = Tk()
pendulum.geometry('560x300')

line = Canvas(pendulum, width=560, height=300)
line.create_line(80, 50, 480, 50)
line.pack()

circle = Canvas(pendulum, width=40, height=40)
circle.create_oval(0, 0, 40, 40, fill='black')
circle.pack()
circle.place(x=270, y=40)

boule = Canvas(pendulum, width=120, height=120)
boule.create_oval(0, 0, 120, 120, fill='black')
boule.pack()

class Timer:
    def __init__(self, interval, function):
        self.interval = interval
        self.function = function

    def start(self):
        pass

    def stop(self):
        pass

animation = Animation(pendulum, 0.0, boule, 200.0)

animation.mytimer.start()

def destroy():
    animation.unlink()
    pendulum.destroy()

pendulum.protocol('WM_DELETE_WINDOW', destroy)

pendulum.mainloop()