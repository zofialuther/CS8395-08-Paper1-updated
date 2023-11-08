```python
from hgl import *

def toInt(x):
    return int(round(x))

def pendulum():
    with createWindow("Pendulum animation task", 600, 400, DoubleBuffered, 30) as w:
        dt = 1/30
        t = -3.14159/4
        l = 1
        g = 9.812

        def nextAVT(avt):
            a, v, t = avt
            a_ = - (g / l) * sin(t)
            v_ = v + a_ * dt
            return (a_, v_, t + v_ * dt)

        pts = [(toInt(300 + 300 * cos(pi/2 + 0.6*t)), toInt(300 * sin(pi/2 + 0.6*t))) for _, t, _ in iterate(nextAVT, (- (g / l) * sin(t), t, 0))]

        for x, y in pts:
            setGraphic(w, line(300, 0, x, y))
            setGraphic(w, ellipse(x - 12, y + 12, x + 12, y - 12))
            getWindowTick(w)
```