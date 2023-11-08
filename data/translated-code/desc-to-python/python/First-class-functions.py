def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def compose(f, g):
    return lambda x: f(g(x))

def curry(f):
    return lambda x: lambda y: f(x, y)

def flip(f):
    return lambda x, y: f(y, x)

def custom_zip(f, list1, list2):
    return [f(x, y) for x, y in zip(list1, list2)]

def main():
    functions = [add, subtract, multiply]
    composed_function = compose(compose(functions[0], curry(functions[1])(3)), flip(functions[2]))
    numbers = [1, 2, 3, 4, 5]
    result = [composed_function(n) for n in numbers]
    print(result)

main()