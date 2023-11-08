from math import sin, cos, tan, pi

def compose(f, g):
    return lambda x: f(g(x))

def cube(x):
    return x ** 3

def cube_root(x):
    return x ** (1/3)

def first_class(values, composed_function):
    results = [composed_function(value) for value in values]
    print(results)

composed_functions = compose(sin, cube_root)
composed_functions = compose(composed_functions, cos)
composed_functions = compose(composed_functions, cube)
values = [1, 2, 3, 4, 5]
first_class(values, composed_functions)