def arithmetic(x, y):
    for op in "+ - * // % **".split():
        expr = f"{x} {op} {y}"
        print(f"{expr}\t=> {eval(expr)}")

arithmetic(12, 8)
arithmetic(int(input("Number 1: ")), int(input("Number 2: ")))