from functools import reduce

def romanFromInt(n):
    def go(a, ms):
        q, r = divmod(a, ms)
        return (r, ms * q)
    return concat(mapAccumL(go, n, [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]))

def main():
    for i in range(1, 21):
        print(romanFromInt(i))

def concat(xxs):
    if isinstance(xxs, str):
        return ''
    elif xxs == []:
        return []
    else:
        return reduce(lambda acc, x: acc + x, xxs)

def mapAccumL(f):
    def go(a, x):
        tpl = f(a[0], x)
        return (tpl[0], a[1] + [tpl[1]])
    return lambda acc, xs: reduce(go, xs, (acc, []))

def snd(tpl):
    return tpl[1]

if __name__ == "__main__":
    main()