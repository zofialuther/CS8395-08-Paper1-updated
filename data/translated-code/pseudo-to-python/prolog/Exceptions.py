def foo(X):
    if not isinstance(X, int):
        raise ValueError('not even an int')
    elif not 1 <= X <= 10:
        raise ValueError('must be between 1 & 10')
    else:
        print(X, 'is a valid number')

def go(X):
    try:
        foo(X)
    except Exception as E:
        if isinstance(E, ValueError):
            print(E)
        else:
            raise E