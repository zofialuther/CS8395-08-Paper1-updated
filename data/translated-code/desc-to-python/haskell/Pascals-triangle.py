def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def binCoef(n, k):
    return fac(n) // (fac(k) * fac(n-k))

def pascal(row):
    pascal_row = []
    for i in range(row+1):
        pascal_row.append(binCoef(row, i))
    return pascal_row