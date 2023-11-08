from math import sin, cos

def compose(F, G):
    return lambda x: G(F(x))

def cube(x):
    return x ** 3

def cube_root(x):
    return x ** (1/3)

def first_class():
    L = [sin, cos, cube]
    IL = [lambda x: asin(x), lambda x: acos(x), cube_root]

    # we create the composed functions
    Lst = [compose(f, g) for f, g in zip(L, IL)]

    # we call the functions
    R = [f(0.5) for f in Lst]

    # we display the results
    for r in R:
        print(r)

first_class()