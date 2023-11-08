def sierpinski(n):
    xs = ["*"]
    for i in range(n):
        s = " " * (2**i)
        xs = list(map(lambda x: [s + x + s], xs)) + list(map(lambda x: [x + ' ' + x], xs))
    return '\n'.join([''.join(row) for row in xs])

def concatMap(f):
    return lambda xs: sum(map(f, xs), [])