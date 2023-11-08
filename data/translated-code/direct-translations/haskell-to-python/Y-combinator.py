def fix(f):
    return f(fix(f))

def fac(n):
    def inner(f, n, i):
        if i <= 0:
            return n
        else:
            return f(i * n, i - 1)
    return fix(inner)(1, n)

def fib(n):
    def inner(fnc, f, s, i):
        if i <= 1:
            return f
        else:
            return fnc(s, f + s, i - 1)
    return fix(inner)(0, 1, n)

def fibs():
    def inner(fnc, f, s):
        result = f + s
        return [result] + fnc(s, result)
    return [0, 1] + fix(inner)(0, 1)

def main():
    results = [list(map(fac, range(1, 21))),
               list(map(fib, range(1, 21))),
               fibs()[:20]]
    for result in results:
        for item in result:
            print(item)

main()