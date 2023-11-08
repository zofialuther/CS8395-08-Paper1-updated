from sympy import primerange, isprime

def primeDecomp(a):
    if a < 2:
        return None
    result = []
    while a % 2 == 0:
        a = a // 2
        result.append(2)
    if a != 1:
        b = 3
        while b < a:
            if isprime(b):
                dr = divmod(a, b)
                if dr[1] == 0:
                    result.append(b)
                    a = dr[0]
            b += 2
        result.append(b)
    return result

def isSemi(x):
    decomp = primeDecomp(x)
    return decomp is not None and len(decomp) == 2

for i in range(2, 101):
    if isSemi(i):
        print(i, end=" ")
print()

for i in range(1675, 1681):
    if isSemi(i):
        print(i, end=" ")
print()