def foo(X):
    if not isinstance(X, int):
        raise Exception('not even an int')
    elif not 1 <= X <= 10:
        raise Exception('must be between 1 & 10')
    else:
        print(f'{X} is a valid number')

def go(X):
    try:
        foo(X)
    except Exception as e:
        handle(e)

def handle(e):
    if isinstance(e, str):
        print(e)
    else:
        raise e