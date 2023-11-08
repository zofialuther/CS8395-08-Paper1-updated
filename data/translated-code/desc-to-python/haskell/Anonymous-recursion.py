def fib(n):
    if n <= 0:
        return None
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return a

numbers = list(range(-4, 11))
result = list(map(lambda x: fib(x), numbers))
print(result)