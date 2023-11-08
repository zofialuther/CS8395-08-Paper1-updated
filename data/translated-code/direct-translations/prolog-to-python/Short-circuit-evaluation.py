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

def a_and_b(x, y):
    print(f'a({x}) and b({y})')
    return a(x) and b(y)

def a_or_b(x, y):
    print(f'a({x}) or b({y})')
    return a(x) or b(y)

def a(x):
    print(f'a({x})')
    return x

def b(x):
    print(f'b({x})')
    return x