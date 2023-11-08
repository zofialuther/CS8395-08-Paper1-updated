def main():
    print(take(8, happyNumbers()))

def happyNumbers():
    x = 1
    while True:
        x = until(isHappy, succ, x)
        yield x
        x = succ(x)

def isHappy(n):
    seen = set()

    def p(x):
        if 1 == x or x in seen:
            return True
        else:
            seen.add(x)
            return False

    def f(x):
        return sum(int(d)**2 for d in str(x))

    return 1 == until(p, f, n)

def succ(x):
    return 1 + x

def take(n, xs):
    if isinstance(xs, list):
        return xs[0:n]
    else:
        return list(islice(xs, n))

def until(p, f, x):
    v = x
    while not p(v):
        v = f(v)
    return v

if __name__ == '__main__':
    main()