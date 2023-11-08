def sum35a(n):
    total = 0
    for x in range(n):
        if x % 3 == 0 or x % 5 == 0:
            total = total + x
    return total

def sum35b(n):
    total = sum(range(3, n, 3)) + sum(range(5, n, 5)) - sum(range(15, n, 15))
    return total

def sum35c(n):
    consts = [3, 5, 15]
    divs = []
    sums = []
    for c in consts:
        divs.append((n-1) / c)
    for i in range(len(divs)):
        sums.append(divs[i] * consts[i] * (1 + divs[i]) / 2)
    return sums[0] + sums[1] - sums[2]

for n in range(1001):
    sa = sum35a(n)
    sb = sum35b(n)
    sc = sum35c(n)
    if sa == sb == sc:
        print("For n = %7i -> %i\n" % (n, sc))

for p in range(7):
    print("For n = %7i -> %i" % (10**p, sum35c(10**p)))

p = 20
print("For n = %20i -> %i" % (10**p, sum35c(10**p)) )