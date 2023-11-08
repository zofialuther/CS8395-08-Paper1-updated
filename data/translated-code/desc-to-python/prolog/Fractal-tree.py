import turtle

def drawTree(t, branchLen, angle, depth):
    if depth > 0:
        t.forward(branchLen)
        t.right(angle)
        drawTree(t, branchLen-15, angle, depth-1)
        t.left(angle*2)
        drawTree(t, branchLen-15, angle, depth-1)
        t.right(angle)
        t.backward(branchLen)

t = turtle.Turtle()
myWin = turtle.Screen()
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
drawTree(t, 75, 20, 9)
myWin.exitonclick()