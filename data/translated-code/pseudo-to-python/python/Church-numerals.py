def churchZero():
    return lambda f: identity

def churchSucc(cn):
    return lambda f: Compose(f)(cn(f))

def churchAdd(m):
    return lambda n: lambda f: Compose(m(f))(n(f))

def churchMult(m):
    return lambda n: Compose(m)(n)

def churchExp(m):
    return lambda n: n(m)

def churchFromInt(n):
    return lambda f: Foldl(Compose)(identity)(Replicate(n)(f))

def churchFromInt_(n):
    if 0 == n:
        return churchZero()
    else:
        return churchSucc(churchFromInt(n - 1))

def intFromChurch(cn):
    return cn(Succ)(0)

def main():
    cThree = churchFromInt(3)
    cFour = churchFromInt(4)

    print(list(map(intFromChurch, [
        churchAdd(cThree)(cFour),
        churchMult(cThree)(cFour),
        churchExp(cFour)(cThree),
        churchExp(cThree)(cFour),
    ]))

def Compose(f):
    return lambda g: lambda x: g(f(x))

def Foldl(f):
    return lambda acc: lambda xs: go(acc, xs)
        def go(acc, xs):
            return reduce(lambda a, x: f(a)(x), xs, acc)

def Identity(x):
    return x

def Replicate(n):
    return lambda x: repeat(x, n)

def Succ(x):
    return 1 + x if isinstance(x, int) else (
        chr(1 + ord(x))
    )