def compose(f, g):
    return lambda x: f(g(x))

def main():
    sin_asin = compose(math.sin, math.asin)
    print(sin_asin(0.5))