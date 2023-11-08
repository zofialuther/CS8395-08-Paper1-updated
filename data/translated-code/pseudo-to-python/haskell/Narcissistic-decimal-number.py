def narcissiOfLength(nDigits):
    powers = list(map(lambda x: x ** nDigits, list(range(0, 10))))
    
    def go(n, parents):
        if n > 0:
            return go(n - 1, f(parents))
        else:
            return list(filter(lambda x: isDaffodil(nDigits, x[1]), parents))
    return go

def f(parents):
    if not parents:
        return powers
    else:
        return [pwrSum + p for p in powers[:parents[0] + 1] for pwrSum in parents]

def isDaffodil(e, n):
    return e == len(digitList(n)) and n == powerSum(e, digitList(n))

def powerSum(n, lst):
    result = 0
    for number in lst:
        result += number ** n
    return result

def digitList(n):
    if n == 0:
        return [0]
    else:
        result = []
        x = n
        while x > 0:
            result.append(x % 10)
            x = x // 10
        return result

def main():
    print(fTable("Narcissistic decimal numbers of length 1-7:\n", show, show, narcissiOfLength, list(range(1, 8)))

def fTable(s, xShow, fxShow, f, xs):
    def rjust(n, char):
        def func(s):
            return s.rjust(n, char)
        return func
    
    w = max([len(xShow(x)) for x in xs])
    return '\n'.join([s] + [rjust(w, ' ')(xShow(x)) + " -> " + fxShow(f(x)) for x in xs])