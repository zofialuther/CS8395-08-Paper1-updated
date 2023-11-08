def compose(f, g):
    def inner(x):
        return f(g(x))
    return inner