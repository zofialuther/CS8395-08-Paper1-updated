```python
from itertools import product

def calculate(tokens, context):
    def interprete(s, op):
        if op == "&":
            x, y, *rest = s
            return rest + [x and y]
        elif op == "|":
            x, y, *rest = s
            return rest + [x or y]
        elif op == "^":
            x, y, *rest = s
            return rest + [x != y]
        elif op == "=>":
            x, y, *rest = s
            return rest + [not y or x]
        elif op == "!":
            x, *rest = s
            return rest + [not x]
        else:
            return rest + [context[op]]

    return foldM(interprete, [], tokens)

def truthTable(expr):
    tokens = expr.split()
    operators = ["&", "|", "!", "^", "=>"]
    variables = list(set(filter(lambda x: x not in operators, tokens)))
    table = list(product([True, False], repeat=len(variables)))
    results = [list(vals) + calculate(tokens, dict(zip(variables, vals))) for vals in table]
    header = variables + ["result"]
    return showTable([header] + [[str(val) for val in row] for row in results])

def showTable(tbl):
    colWidth = max(6, max(len(cell) for row in tbl for cell in row))
    return "\n".join([" ".join(cell.ljust(colWidth) for cell in row) for row in tbl])

while True:
    expr = input()
    print(truthTable(expr))
```