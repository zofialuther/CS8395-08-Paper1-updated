from math import pow

def nthroot(num, n):
    return pow(num, 1/n)

print(round(nthroot(34, 5), 10))
print(round(nthroot(42, 10), 20))
print(round(nthroot(5, 2), 400))