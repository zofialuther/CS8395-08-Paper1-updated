def make_lambda(i):
    return lambda: i

funcs = [make_lambda(i * i) for i in range(10)]
print(funcs[3]()) # prints 9