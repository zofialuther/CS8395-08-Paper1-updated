def short_circuit():
    if a_or_b(True, True):
        print('==> true')
    else:
        print('==> false')
    print()
    
    if a_or_b(True, False):
        print('==> true')
    else:
        print('==> false')
    print()
    
    if a_or_b(False, True):
        print('==> true')
    else:
        print('==> false')
    print()
    
    if a_or_b(False, False):
        print('==> true')
    else:
        print('==> false')
    print()
    
    if a_and_b(True, True):
        print('==> true')
    else:
        print('==> false')
    print()
    
    if a_and_b(True, False):
        print('==> true')
    else:
        print('==> false')
    print()
    
    if a_and_b(False, True):
        print('==> true')
    else:
        print('==> false')
    print()
    
    if a_and_b(False, False):
        print('==> true')
    else:
        print('==> false')
    print()

def a_and_b(X, Y):
    print(f'a({X}) and b({Y})')
    return a(X) and b(Y)

def a_or_b(X, Y):
    print(f'a({X}) or b({Y})')
    return a(X) or b(Y)

def a(X):
    print(f'a({X})')
    return X

def b(X):
    print(f'b({X})')
    return X