def numeric(X):
    if 48 <= X and X <= 57:
        return True
    else:
        return False

def not_numeric(X):
    if 48 > X or X > 57:
        return True
    else:
        return False

def lex1(Xs, Ys):
    return

def lex1(Xs, Ys):
    if Xs[0] == 40:
        lex1(Xs[1:], Ys + ['('])
    elif Xs[0] == 41:
        lex1(Xs[1:], Ys + [')'])
    elif Xs[0] == 43:
        lex1(Xs[1:], Ys + ['+'])
    elif Xs[0] == 45:
        lex1(Xs[1:], Ys + ['-'])
    elif Xs[0] == 42:
        lex1(Xs[1:], Ys + ['*'])
    elif Xs[0] == 47:
        lex1(Xs[1:], Ys + ['/'])
    elif numeric(Xs[0]):
        N = Xs[0] - 48
        lex1(Xs[1:], Ys + [N])

def lex2(Xs, Ys):
    return

def lex2(Xs, Ys):
    if len(Xs) == 1:
        return [Xs[0]]
    elif len(Xs) >= 2:
        if (type(Xs[0]) == str or (isinstance(Xs[0], int) and type(Xs[1]) == str)):
            lex2(Xs[1:], Ys + [Xs[0]])
        elif isinstance(Xs[0], int) and isinstance(Xs[1], int):
            N = Xs[0] * 10 + Xs[1]
            lex2([N] + Xs[2:], [Y] + Ys)

def oper(N, Op, X, Y):
    if N == 1 and Op == '*':
        return X * Y
    elif N == 1 and Op == '/':
        return X / Y
    elif N == 2 and Op == '+':
        return X + Y
    elif N == 2 and Op == '-':
        return X - Y

def num(D):
    return [D], [isinstance(D, int)]

def expr(N, Z):
    if N == 0 and isinstance(Z, int):
        return [Z], True
    elif N == 0 and Z[0] == '(' and Z[-1] == ')':
        return expr(2, Z[1:-1])
    elif N != 0 and (isinstance(Z[0], int) or (isinstance(Z[0], str) and isinstance(Z[1], int))):
        X = oper(N, Z[1], Z[0], Z[2])
        return expr(N-1, X)
    elif N != 0:
        return expr(N-1, Z)

def parse(Tokens, Expr):
    return expr(2, Expr, Tokens, [])

def evaluate(E, E):
    if isinstance(E, int):
        return
    elif E[1] == '+':
        A = evaluate(E[0])
        B = evaluate(E[2])
        E = A + B
    elif E[1] == '-':
        A = evaluate(E[0])
        B = evaluate(E[2])
        E = A - B
    elif E[1] == '*':
        A = evaluate(E[0])
        B = evaluate(E[2])
        E = A * B
    elif E[1] == '/':
        A = evaluate(E[0])
        B = evaluate(E[2])
        E = A / B

def calculator(String, Value):
    Codes = list(map(ord, String))
    Tokens1 = lex1(Codes, [])
    Tokens2 = lex2(Tokens1, [])
    Expression = parse(Tokens2, [])
    evaluate(Expression, Value)
    return

# Example use
calculator("(3+50)*7-9", X)