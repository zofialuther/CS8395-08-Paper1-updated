```python
from pce import library

def animation():
    D = library.window('Animation')
    Label = library.label('Hello world ! ')
    D.display(Label, (1,10))
    animation = Animation(Label)
    D.set_recogniser('left click')
    D.set_done_message(free(animation) and destroy(receiver))
    D.open()
    animation.start_timer()

class Animation:
    def __init__(self, label, delta=None, mytimer=None):
        self.label = label
        self.delta = delta
        self.mytimer = mytimer
        
    def initialise(self, P, W):
        P.label = W
        P.delta = to_left
        P.mytimer = library.timer(P, 0.5, anim_message)
        
    def unlink(self, P):
        P.mytimer.stop()
        free(P)
        
    def anim_message(self, P):
        L = P.label
        S = L.selection
        Delta = P.delta
        S1 = compute(Delta, S, S1)
        A = library.object(S1)
        L.selection = A

class my_click_gesture(click_gesture):
    button = 'left'
    
    def terminate(self, G, Ev):
        super().terminate(Ev)
        D = @animation.delta
        if D == to_left:
            D1 = to_right
        else:
            D1 = to_left
        @animation.delta = D1

def compute(to_right, S, S1):
    Len = len(S)
    Len1 = Len - 1
    Str = S[Len1:]
    V = S[:-Len1]
    S1 = V + Str

def compute(to_left, S, S1):
    Str = S[0:1]
    V = S[1:]
    S1 = V + Str
```