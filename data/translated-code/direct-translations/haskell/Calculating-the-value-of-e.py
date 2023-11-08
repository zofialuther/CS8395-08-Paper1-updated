def eApprox(n):
    return sum((1 / x) for x in range(1, n+1))

# TEST
print(eApprox(20))