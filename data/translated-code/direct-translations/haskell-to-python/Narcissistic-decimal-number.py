```python
def narcissiOfLength(nDigits):
    powers = [(d, d ** nDigits) for d in range(10)]
    
    def go(n, parents):
        if n > 0:
            return go(n - 1, f(parents))
        else:
            return [p[1] for p in parents if isDaffodil(nDigits, p[1])]
    
    def f(parents):
        if not parents:
            return powers
        else:
            return [(d, pwrSum + power) for (d, pwrSum) in parents for power in powers[:d+1]]
    
    return list(map(lambda x: x[1], go(nDigits, [])))


def isDaffodil(e, n):
    return e == len(str(n)) and n == powerSum(e, list(map(int, str(n))))


def powerSum(n, digits):
    return sum([digit ** n for digit in digits])


def digitList(n):
    if n == 0:
        return [0]
    else:
        return [int(x) for x in str(n)]


def main():
    def fTable(s, xShow, fxShow, f, xs):
        def rjust(n, c):
            return lambda x: (c * (n - len(x)) + x)

        w = max(len(xShow(x)) for x in xs)
        print(s)
        for x in xs:
            print(rjust(w, ' ')(xShow(x)) + " -> " + fxShow(f(x)))

    fTable("Narcissistic decimal numbers of length 1-7:\n", str, str, narcissiOfLength, list(range(1, 8)))


main()
```