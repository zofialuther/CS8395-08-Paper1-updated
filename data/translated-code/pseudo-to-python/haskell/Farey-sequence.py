```python
def farey(n):
    result = [0]
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = (n + b) / d
        result.append(c / d)
        a = c
        b = d
        c = k * c - a
        d = k * d - b
    return result

def fareys(fn, ns):
    result = []
    rs = farey(ns[-1])
    for n in reversed(ns):
        rs_ = filter(lambda x: x[1] <= n, rs)
        rs = rs_
        result.append((n, fn(rs_)))
    return result

def fprint(fmt, pairs):
    for pair in pairs:
        print(fmt % pair)

def showFracs(fracs):
    result = ""
    for frac in fracs:
        result += str(frac.numerator) + "/" + str(frac.denominator) + " "
    return result

def main():
    print("Farey Sequences\n")
    fprint("%2d %s\n", fareys(showFracs, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print("\nSequence Lengths\n")
    fprint("%4d %d\n", fareys(len, [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))

main()
```