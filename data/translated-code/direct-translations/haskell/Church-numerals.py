```python
class Church:
    def __init__(self, unChurch):
        self.unChurch = unChurch

def churchZero():
    return Church(lambda f: lambda x: x)

def succChurch(ch):
    return Church(lambda f: lambda x: f(ch.unChurch(f)(x)))

def addChurch(ach, bch):
    return Church(lambda f: lambda x: ach.unChurch(f)(bch.unChurch(f)(x)))

def multChurch(ach, bch):
    return Church(lambda f: lambda x: ach.unChurch(bch.unChurch(f))(x))

def expChurch(basech, expch):
    return Church(lambda f: lambda x: expch.unChurch(basech.unChurch)(f)(x))

def predChurch(ch):
    return Church(lambda f: lambda x: ch.unChurch(lambda g: lambda h: h(g(f)))(lambda x: x)(lambda x: x))

def minusChurch(ach, bch):
    return bch.unChurch(predChurch)(ach)

def isChurchZero(ch):
    return ch.unChurch(lambda x: churchZero())(Church(lambda x: x))

def divChurch(dvdnd, dvsr):
    def divr(n):
        return (lambda v: v.unChurch(lambda x: succChurch(divr(x)))(churchZero))(minusChurch(n, dvsr))
    return divr(succChurch(dvdnd))

def churchFromInt(n):
    if n == 0:
        return churchZero()
    else:
        return succChurch(churchFromInt(n - 1))

def intFromChurch(ch):
    return ch.unChurch(lambda x: x + 1)(0)

# TEST
def main():
    cThree = churchFromInt(3)
    cFour = churchFromInt(4)
    cEleven = churchFromInt(11)
    cTwelve = churchFromInt(12)
    result = [intFromChurch(addChurch(cThree, cFour)),
              intFromChurch(multChurch(cThree, cFour)),
              intFromChurch(expChurch(cFour, cThree)),
              intFromChurch(expChurch(cThree, cFour)),
              intFromChurch(isChurchZero(churchZero())),
              intFromChurch(predChurch(cFour)),
              intFromChurch(minusChurch(cEleven, cThree)),
              intFromChurch(divChurch(cEleven, cThree)),
              intFromChurch(divChurch(cTwelve, cThree))]
    print(result)

main()
```