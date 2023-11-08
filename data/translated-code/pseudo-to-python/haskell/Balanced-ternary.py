```python
def zeroTrim(a):
    if a is None:
        return [0]
    else:
        return a

def btList(a):
    return a

def equal(a, b):
    return btList(a) == btList(b)

def btNormalize():
    return listBt(_carry(0))

def _carry(c, a):
    if c == 0:
        return []
    else:
        return [c]
    if a == []:
        return r:_carry(cc, as)
    else:
        (cc, r) = f((a + c) / 3)
        def f(x, y):
            if y == 2:
                return (x + 1, -1)
            elif y == -2:
                return (x - 1, 1)
            else:
                return x

def listBt():
    return Bt(zeroTrim)

def show():
    return reverse(map(lambda d: '-' if d == -1 else '0' if d == 0 else '+' btList))

def strBt():
    return Bt(zeroTrim.reverse.map(lambda c: -1 if c == '-' else 0 if c == '0' else 1))

def intBt(a):
    return fromIntegral(toInteger(a))

def btInt():
    return foldr(lambda a, z: a + 3 * z, 0, btList)

def listAdd(a, b):
    return take(max(length(a), length(b)), zipWith(lambda x, y: x + y, a + [0, 0..], b + [0, 0..]))

def negate():
    return Bt(map(negate, btList))

def addition(x, y):
    return btNormalize(listAdd(btList(x), btList(y)))

def multiplication(x, y):
    def mul_(as, b):
        if b == []:
            return []
        else:
            return foldr(lambda a, z: listAdd(map(lambda a: a * b, b)(0:z), [], as)
    return btNormalize(mul_(btList(x), btList(y)))

def signum(a):
    if a == [0]:
        return 0
    else:
        return Bt([last(a)])

def absolute(x):
    if signum(x) == Bt([-1]):
        return negate(x)
    else:
        return x

def fromInteger(x):
    def f(x):
        if x == 0:
            return []
        else:
            return fromInteger(rem(x, 3)) + f(quot(x, 3))
    return btNormalize(f(x))

def main():
    (a, b, c) = (strBt("+-0++0+"), intBt(-436), strBt("+-++-"))
    r = multiplication(a, addition(b, c))
    print(list(map(btInt, [a, b, c]))
    print(r)
    print(btInt(r))
```