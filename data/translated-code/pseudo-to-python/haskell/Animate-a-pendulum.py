from math import sin, cos, pi, round
from time import sleep
from hgl import *  # Replace with appropriate library for graphics

def toInt(num):
    return int(round(num))

def nextAVT(a, v, t, dt, l, g):
    a_prime = - (g / l) * sin(t)
    v_prime = v + a_prime * dt
    t_prime = t + v_prime * dt
    return (a_prime, v_prime, t_prime)

def calculatePts(l, g, dt):
    t = - pi/4
    pts = []
    for i in range(30):
        (a, t, _) = nextAVT(- (g / l) * sin(t), t, 0, dt, l, g)
        x = toInt(300 + (300 * cos(pi/2 + 0.6 * t)))
        y = toInt(300 * sin(pi/2 + 0.6 * t))
        pts.append((x, y))
    return pts

def pendulumAnimation():
    window = openWindowEx("Pendulum animation task", None, (600, 400), DoubleBuffered, 30)
    for pts in calculatePts(1, 9.812, 1/30):
        x = pts[0]
        y = pts[1]
        line = createLine(300, 0, x, y)
        ellipse = createEllipse(x - 12, y + 12, x + 12, y - 12)
        setGraphic(window, overGraphic(line, ellipse))
        getWindowTick(window)
        sleep(0.03)
    closeWindow(window)

pendulumAnimation()