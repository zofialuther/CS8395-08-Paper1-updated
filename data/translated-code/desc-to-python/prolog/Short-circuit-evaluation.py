def a(x):
    print(x)
    return x

def b(y):
    print(y)
    return y

def a_and_b(x, y):
    return a(x) and b(y)

def a_or_b(x, y):
    return a(x) or b(y)

def short_circuit(x, y):
    print(a_and_b(x, y))
    print(a_or_b(x, y))

short_circuit(True, False)