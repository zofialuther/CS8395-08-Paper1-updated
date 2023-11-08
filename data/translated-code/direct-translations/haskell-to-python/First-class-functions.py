def cube(x):
    return x ** 3.0

def croot(x):
    return x ** (1/3)

funclist = [sin, cos, cube]

invlist = [asin, acos, croot]

def main():
    print(list(map(lambda f, i: f(i(0.5)), funclist, invlist)))

main()