def F(n):
    if n == 0:
        return 1
    else:
        return n - M(F(n-1))

def M(n):
    if n == 0:
        return 0
    else:
        return n - F(M(n-1))

print([F(n) for n in range(20)])
print([M(n) for n in range(20)])