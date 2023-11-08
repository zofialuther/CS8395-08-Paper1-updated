def truthTable(expr):
    tokens = expr.split(" ")
    operators = ["&", "|", "!", "^", "=>"]
    variables = list(set(filter(lambda token: token not in operators, tokens)))
    table = list(zip(variables, map(lambda var: [True, False], variables))
    results = list(map(lambda r: list(map(lambda x: x[1], r)) + [calculate(tokens, r)], table)
    header = variables + ["result"]
    showTable(header + list(map(lambda r: list(map(lambda x: str(x), r)), results))

def calculate(tokens, context):
    return functools.reduce(interprete, tokens, [])
    
def interprete(s, op, x, y=None):
    if op == "&":
        return s + [x and y]
    elif op == "|":
        return s + [x or y]
    elif op == "^":
        return s + [x != y]
    elif op == "=>":
        return s + [not y or x]
    elif op == "!":
        return s + [not x]
    else:
        return s + [context[x]]

def showTable(tbl):
    return "\n".join(map(lambda row: " ".join(map(align, row)), tbl))
    
def align(txt):
    colWidth = max(6, max(map(len, tbl[0])))
    return (txt + " " * colWidth)[:colWidth]