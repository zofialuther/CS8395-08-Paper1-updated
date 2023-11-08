```python
# Lexer
def numeric(X):
    return 48 <= X <= 57

def not_numeric(X):
    return 48 > X or X > 57

def lex1(Xs, Ys):
    if Xs == []:
        return Ys
    elif Xs[0] == 40:
        return ['('] + lex1(Xs[1:], Ys)
    elif Xs[0] == 41:
        return [')'] + lex1(Xs[1:], Ys)
    elif Xs[0] == 43:
        return ['+'] + lex1(Xs[1:], Ys)
    elif Xs[0] == 45:
        return ['-'] + lex1(Xs[1:], Ys)
    elif Xs[0] == 42:
        return ['*'] + lex1(Xs[1:], Ys)
    elif Xs[0] == 47:
        return ['/'] + lex1(Xs[1:], Ys)
    else:
        if numeric(Xs[0]):
            N = Xs[0] - 48
            return [N] + lex1(Xs[1:], Ys)

def lex2(Xs, Ys):
    if Xs == []:
        return Ys
    elif len(Xs) == 1:
        return Ys + [Xs[0]]
    elif isinstance(Xs[0], str) and isinstance(Xs[1], str):
        return lex2(Xs[1:], Ys + [Xs[0]])
    elif isinstance(Xs[0], int) and isinstance(Xs[1], str):
        return lex2(Xs[1:], Ys + [Xs[0]])
    elif isinstance(Xs[0], int) and isinstance(Xs[1], int):
        N = Xs[0] * 10 + Xs[1]
        return lex2([N] + Xs[2:], Ys)

# Parser
def oper(N, Op, X, Y, Z):
    if N == 1:
        if Op == '*':
            return X * Y
        elif Op == '/':
            return X / Y
    elif N == 2:
        if Op == '+':
            return X + Y
        elif Op == '-':
            return X - Y

def num(D):
    if isinstance(D, int):
        return [D]

def expr(N, Z, Tokens):
    if N == 0:
        if isinstance(Z, int):
            return num(Z)
        elif isinstance(Z, tuple):
            X = Z[0]
            return ['('] + expr(2, X, Tokens) + [')']
    else:
        if N > 0:
            N0 = N - 1
            Op = Tokens[1]
            X = Tokens[0]
            Y = Tokens[2]
            Z = oper(N, Op, X, Y, Z)
            return expr(N0, X, Tokens[0]) + [Op] + expr(N, Y, Tokens[2])

def parse(Tokens, Expr):
    return expr(2, Expr, Tokens)

# Evaluator
def evaluate(E):
    if isinstance(E, int):
        return E
    elif isinstance(E, tuple):
        if E[1] == '+':
            return evaluate(E[0]) + evaluate(E[2])
        elif E[1] == '-':
            return evaluate(E[0]) - evaluate(E[2])
        elif E[1] == '*':
            return evaluate(E[0]) * evaluate(E[2])
        elif E[1] == '/':
            return evaluate(E[0]) / evaluate(E[2])

# Solution
def calculator(String):
    Codes = [ord(c) for c in String]
    Tokens1 = lex1(Codes, [])
    Tokens2 = lex2(Tokens1, [])
    Expression = parse(Tokens2)
    Value = evaluate(Expression)
    return Value

# Example use
x = calculator("(3+50)*7-9")
print(x)
```