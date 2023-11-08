def compose(f, g):
    return lambda x: f(g(x))

def main(args):
    functions = []
    functions.append(lambda x: math.cos(x))
    functions.append(lambda x: math.tan(x))
    functions.append(lambda x: x * x)
    
    inverse = []
    inverse.append(lambda x: math.acos(x))
    inverse.append(lambda x: math.atan(x))
    inverse.append(lambda x: math.sqrt(x))
    
    print("Compositions:")
    for i in range(len(functions)):
        print(compose(functions[i], inverse[i])(0.5))
    
    print("Hard-coded compositions:")
    print(math.cos(math.acos(0.5)))
    print(math.tan(math.atan(0.5)))
    print(math.pow(math.sqrt(0.5), 2))