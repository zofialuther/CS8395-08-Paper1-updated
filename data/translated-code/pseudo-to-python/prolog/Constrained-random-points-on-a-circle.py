from constraint import *
import random
import tkinter as tk
import turtle

def circle():
    BL = bagof((X,Y), init(X,Y))
    N = len(BL)
    L = [0]*100
    L = list(map(lambda x: random.choice(BL), L))
    draw_circle(L)

def choose(BL, N, V):
    I = random.randint(0, N-1)
    V = BL[I]

def init(X1, Y1):
    X = Variable(0, 15)
    Y = Variable(0, 15)
    problem = Problem()
    problem.addConstraint(lambda x, y: x**2 + y**2 >= 100, [X, Y])
    problem.addConstraint(lambda x, y: x**2 + y**2 <= 225, [X, Y])
    problem.getSolution()
    X1 = 10*X + 200
    Y1 = 10*Y + 200

def draw_circle(L):
    D = turtle.Turtle()
    D.title('Circle')
    D.setup(400, 400)
    for point in L:
        X = point[0]
        Y = point[1]
        D.penup()
        D.goto(X, Y)
        D.pendown()
        D.circle(4)
        D.fillcolor('black')
    turtle.done()