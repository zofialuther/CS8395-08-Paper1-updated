```python
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.goto(-300, 150)
t.pendown()
t.fillcolor("pink")
t.begin_fill()

for _ in range(3):
    koch_curve(t, 4, 600)
    t.right(120)

t.end_fill()
t.getscreen().getcanvas().postscript(file="koch_curve_fractal.eps")

```