def rpn(L):
    print('Token  Action                             Stack')
    parse(L, [])

def parse(L, St):
    if L:
        X = L[0]
        if X.isspace():
            parse(L[1:], St)
        elif X.isdigit():
            parse_number(L[1:], [X], St)
        else:
            ops = {'*': 42, '+': 43, '-': 45, '/': 47, '^': 94}
            if X in ops:
                op = ops[X]
                V = eval_op(op, St)
                print(f'    {X}  Apply {X} on top of stack  {V}  {St}')
                parse(L[1:], [V] + St)

def parse_number(S, NC, St):
    if S:
        N = S[0]
        if N.isdigit():
            parse_number(S[1:], [N] + NC, St)
        else:
            V = int(''.join(NC))
            print(f'     {V}  Push num {V} on top of stack  {V}  {St}')
            parse(S, [V] + St)

def eval_op(op, St):
    Y = St[0]
    X = St[1]
    if op == 42:
        return X * Y
    elif op == 43:
        return X + Y
    elif op == 45:
        return X - Y
    elif op == 47:
        return X / Y
    elif op == 94:
        return X ** Y
```