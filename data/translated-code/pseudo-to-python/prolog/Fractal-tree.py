```python
import turtle

def fractal():
    D = turtle.Screen()
    D.setup(800, 600)
    drawTree(turtle, 400, 500, -90, 9)
    D.mainloop()
    

def drawTree(t, X, Y, Angle, Depth):
    if Depth == 0:
        return
    X1 = X
    Y1 = Y
    X2 = X1 + math.cos(Angle * math.pi / 180.0) * Depth * 10.0
    Y2 = Y1 + math.sin(Angle * math.pi / 180.0) * Depth * 10.0
    t.penup()
    t.goto(X1, Y1)
    t.pendown()
    t.goto(X2, Y2)
    A1 = Angle - 30
    A2 = Angle + 30
    De = Depth - 1
    drawTree(t, X2, Y2, A1, De)
    drawTree(t, X2, Y2, A2, De)

fractal()
```