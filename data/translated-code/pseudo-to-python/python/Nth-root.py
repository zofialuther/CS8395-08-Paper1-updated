def nthroot(x, n, precision):
    guess = x / 2
    while abs(x - guess**n) > precision:
        guess = guess - (guess**n - x) / (n * guess**(n-1))
    return guess

print(nthroot(5, 34, 10))
print(nthroot(10,42, 20))
print(nthroot(2, 5, 400))