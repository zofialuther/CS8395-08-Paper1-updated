```python
from tkinter import *
import time

class Animation:
    def __init__(self, label):
        self.label = label
        self.delta = 'to_left'
        self.mytimer = Timer(0.5, self.anim_message)

    def anim_message(self):
        S = self.label.cget("text")
        if self.delta == 'to_right':
            S1 = S[:-1]
        else:
            S1 = S[1:]
        self.label.config(text=S1)
        self.label.after(500, self.anim_message)

class MyClickGesture:
    def __init__(self):
        self.button = 'left'

    def terminate(self, event):
        if animation.delta == 'to_left':
            animation.delta = 'to_right'
        else:
            animation.delta = 'to_left'

def animation():
    window = Tk()
    window.title('Animation')
    label = Label(window, text='Hello world !')
    label.place(x=1, y=10)
    animation = Animation(label)
    gesture = MyClickGesture()
    window.bind("<Button-1>", gesture.terminate)
    window.mainloop()

animation()
```