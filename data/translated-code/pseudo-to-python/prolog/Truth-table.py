def truth_table():
    In = input("Enter current input: ")
    Line = In.split()
    A = [char for char in Line]
    Chars = [char for char in A]

    Tok = tok(Chars)
    Expr, Vars = phrase_expr(Tok)
    VarSet = set(Vars)

    print_expr(Expr, VarSet)

def print_expr(Expr, Vars):
    list(map(lambda x: print(format(x)), Vars))
    print("\n")

    Tvals = eval_expr(Expr, Vars)
    list(map(lambda x: print(format(x)), Tvals))
    print("\n")

def tok(As):
    spaces(As)
    chars(As)

def phrase_expr(Tok):
    # implementation of phrase_expr function
    return ["Expr"], ["Vars"]

def chars(Xs):
    # implementation of chars function
    pass

def spaces(Xs):
    # implementation of spaces function
    pass

def eval_expr(Expr, Vars):
    # implementation of eval_expr function
    return ["Tvals"]

# continue with the rest of the code...