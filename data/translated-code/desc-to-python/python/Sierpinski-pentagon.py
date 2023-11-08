import turtle

def pentagon(t, size):
    for i in range(5):
        t.forward(size)
        t.right(72)

def sierpinski(t, order, size):
    if order == 0:
        for i in range(5):
            t.forward(size)
            t.right(72)
    else:
        sierpinski(t, order-1, size/2)
        t.forward(size/2)
        sierpinski(t, order-1, size/2)
        t.backward(size/2)
        t.right(72)
        t.forward(size/2)
        t.left(72)
        sierpinski(t, order-1, size/2)
        t.right(72)
        t.backward(size/2)
        t.left(72)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    t.up()
    t.goto(-50, -200)
    t.down()
    t.fillcolor("black")
    t.begin_fill()
    pentagon(t, 100)
    t.end_fill()
    t.up()
    t.goto(-50, -200)
    t.down()
    t.fillcolor("white")
    sierpinski(t, 4, 100)
    t.hideturtle()
    myWin.exitonclick()

main()