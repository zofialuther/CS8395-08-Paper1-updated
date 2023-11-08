def agm(a, g, eq):
    def step(t):
        x, y = t
        return ((x + y) / 2, (x * y) ** 0.5)
    
    t = (a, g)
    while not eq(t):
        t = step(t)
    
    return t[1]

def relDiff(t):
    x, y = t
    n = abs(x - y)
    d = (abs(x) + abs(y)) / 2
    return n / d

def main():
    equal = lambda x: relDiff(x) < 0.000000001
    print(agm(1, 1 / (2 ** 0.5), equal))

main()