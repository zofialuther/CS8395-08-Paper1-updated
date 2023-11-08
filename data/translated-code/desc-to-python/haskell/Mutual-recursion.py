def f(n):
    if n == 0:
        return 0
    else:
        return n - m(n-1)

def m(n):
    if n == 0:
        return 0
    else:
        return n - f(n-1)

def main():
    for i in range(20):
        print(f(i), m(i))

main()