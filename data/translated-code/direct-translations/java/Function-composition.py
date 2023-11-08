from math import sin, asin

def compose(f, g):
    return lambda x: f(g(x))

def main():
    sin_asin = compose(sin, asin)
    print(sin_asin(0.5)) # prints "0.5"

if __name__ == "__main__":
    main()