import math

def nthroot(n, m, p):
    return round(m ** (1/n), p)

print(nthroot(5, 34, 10))
print(nthroot(10, 42, 20))
print(nthroot(2, 5, 400))