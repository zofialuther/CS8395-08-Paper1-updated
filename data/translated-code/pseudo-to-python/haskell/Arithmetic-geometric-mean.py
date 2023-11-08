def agm(a, g, eq):
    def until(f, x):
        while not f(x):
            x = step(x)
        return x

    def step(p):
        return (p[0] + p[1]) / 2, (p[0] * p[1]) ** 0.5
    
    return until(eq, (a, g))[1]

def relDiff(x, y):
    n = abs(x - y)
    d = (abs(x) + abs(y)) / 2
    return n / d

def main():
    equal = lambda x, y: relDiff(x, y) < 0.000000001
    print(agm(1, 1 / 2**0.5, equal))

main()