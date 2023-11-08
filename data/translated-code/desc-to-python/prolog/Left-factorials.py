def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def leftfact(n):
    if n == 1:
        print(factorial(1))
    else:
        print(factorial(n) + leftfact(n-1)

leftfact(10001)