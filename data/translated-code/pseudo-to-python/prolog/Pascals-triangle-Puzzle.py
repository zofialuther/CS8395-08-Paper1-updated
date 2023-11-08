from constraint import *

problem = Problem()

def puzzle(Ts, X, Y, Z):
    Ts = [[1,0,0],[1,2,0],[1,2,3],[1,2,3,4]]
    Y = X + Z
    triangle(Ts)
    Vs = []
    for i in range(0, infinity):
        Vs.append(i)
    problem.addVariable("Vs", Vs)
    problem.addConstraint(lambda Vs: Vs in range(0, infinity))
    problem.addConstraint(triangle, Ts)

def triangle(Ts):
    if len(Ts) > 1:
        triangle_(Ts[0:2])
        triangle(Ts[1:])
    else:
        return True

def triangle_(list1, list2):
    if len(list1) == 0:
        return True
    else:
        list1[0] = list2[0] + list2[1]
        return triangle_(list1[1:], list2[1:])