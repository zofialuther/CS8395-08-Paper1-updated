def rpn(L):
    print('Token  Action                             Stack')
    parse(L, [], [X], [])
    print('The final output value is', X)

def parse(L, St, X):
    if L:
        if L[0].isspace():
            parse(L[1:], St, X)
        elif L[0] in ['*', '+', '-', '/', '^']:
            op = L[0]
            Y, X = St.pop(), St.pop()
            V = is_op(op, X, Y)
            print(f'    {op}', end='')
            print(f'  Apply {op} on top of stack', end='')
            print(f'  {V} {St}')
            parse(L[1:], St + [V], X)
        elif L[0].isdigit():
            parse_number(L, [L[0]], St, X)
    else:
        X = St

def parse_number(L, NC, St, X):
    if L and L[0].isdigit():
        parse_number(L[1:], [L[0]] + NC, St, X)
    else:
        V = int(''.join(NC[::-1]))
        print(f'    {V}', end='')
        print(f'  Push num {V} on top of stack', end='')
        print(f'  {V} {St}')
        parse(L, St + [V], X)

def is_op(op, X, Y):
    if op == '*':
        return X * Y
    elif op == '+':
        return X + Y
    elif op == '-':
        return X - Y
    elif op == '/':
        return X / Y
    elif op == '^':
        return X ** Y