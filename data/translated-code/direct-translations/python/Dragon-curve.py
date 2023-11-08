import turtle

def dragon(step, length):
    dcr(step, length)

def dcr(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        turtle.right(45)
        dcr(step, length)
        turtle.left(90)
        dcl(step, length)
        turtle.right(45)
    else:
        turtle.right(45)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(45)

def dcl(step, length):
    step -= 1
    length /= 1.41421

    if step > 0:
        turtle.left(45)
        dcr(step, length)
        turtle.right(90)
        dcl(step, length)
        turtle.left(45)
    else:
        turtle.left(45)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(45)