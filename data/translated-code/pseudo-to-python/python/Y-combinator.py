def Y(f):
    def inner(x):
        def inner2(y):
            return f(lambda *args: y(y)(*args))
        return x(x)(inner2)
    return inner

def fac(f):
    def inner(n):
        if n < 2:
            return 1
        else:
            return n * f(n-1)
    return inner

result1 = [0] * 10
for i in range(10):
    result1[i] = Y(fac)(i)

def fib(f):
    def inner(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return f(n-1) + f(n-2)
    return inner

result2 = [0] * 10
for i in range(10):
    result2[i] = Y(fib)(i)