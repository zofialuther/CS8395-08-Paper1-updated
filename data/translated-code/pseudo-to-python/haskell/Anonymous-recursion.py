def fib(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            next_num = a + b
            a = b
            b = next_num
        return b

result = list(map(fib, list(range(-4, 11))))
print(result)