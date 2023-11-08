def arithmetic(x, y):
    for op in ["+", "-", "*", "//", "%", "**"]:
        expr = str(x) + op + str(y)
        print(expr + " => " + str(eval(expr))

arithmetic(12, 8)
arithmetic(int(input("Number 1: ")), int(input("Number 2: ")))