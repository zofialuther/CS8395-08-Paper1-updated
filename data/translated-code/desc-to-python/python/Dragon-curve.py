import turtle

def dragon(step, length):
    def dcr(step, length):
        if step > 0:
            dcr(step - 1, length / 1.41421)
            turtle.right(45)
            dcl(step - 1, length / 1.41421)
            turtle.forward(length)
        else:
            turtle.forward(length)
            turtle.right(45)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.right(45)

    def dcl(step, length):
        if step > 0:
            turtle.right(45)
            dcr(step - 1, length / 1.41421)
            turtle.forward(length)
            dcl(step - 1, length / 1.41421)
            turtle.left(45)
        else:
            turtle.right(45)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.right(45)

    dcr(step, length)

turtle.speed(0)
turtle.hideturtle()
dragon(10, 200)
turtle.done()