```python
# Step 1 - tokenize the input into spaces, brackets and atoms
def tok(chars):
    if chars[0] == ' ':
        chars = chars[1:]
    if chars[0] == '(' or chars[0] == ')':
        return [chars[0]] + tok(chars[1:])
    else:
        token = ''
        while chars and chars[0] != ' ' and chars[0] != '(' and chars[0] != ')':
            token += chars[0]
            chars = chars[1:]
        return [token] + tok(chars)

# Step 2 - Parse the expression into an evaluable term
def expr(chars):
    def starter(chars):
        if chars[0] == 'not':
            return ['not'] + starter(chars[1:])
        elif chars[0] == '(':
            tokens, vars = expr(chars[1:])
            return ['('] + tokens + starter(chars[1+len(tokens):])
        else:
            return [chars[0]], [chars[0]]

    if chars[0] == 'not':
        tokens, vars = expr(chars[1:])
        infix, vars2 = expr(chars[1+len(tokens):])
        return ['op', 'not', tokens, infix], vars + vars2
    elif chars[0] == '(':
        tokens, vars = expr(chars[1:])
        infix, vars2 = expr(chars[1+len(tokens):])
        return ['(', tokens, infix], vars + vars2
    else:
        return [chars[0]], [chars[0]]

# Step 3 - evaluate the parsed expression
def eval_expr(expr, vars):
    tvals = [[0, 0, 0], [0, 0, 1]]
    results = []
    for tval in tvals:
        results.append(eval(expr, vars, tval))
    return results

def eval(x, vars, vals):
    if x in vars:
        return vals[vars.index(x)]
    elif x[0] == 'op':
        if x[1] == 'not':
            return e('not', eval(x[2], vars, vals))
        else:
            return e(x[1], eval(x[2], vars, vals), eval(x[3], vars, vals))

def e(op, a, b=None):
    if op == 'or':
        return a or b
    elif op == 'and':
        return a and b
    elif op == 'xor':
        return a != b
    elif op == 'nand':
        return not (a and b)
    elif op == 'not':
        return not a

print(eval_expr(expr(tok('not a and (b or c)')), ['a', 'b', 'c']))
```