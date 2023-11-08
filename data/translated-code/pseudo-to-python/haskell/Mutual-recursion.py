def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return n - m(f(n-1))

def m(n):
    if n == 0:
        return 0
    elif n > 0:
        return n - f(m(n-1))

def main():
    for i in range(20):
        print(f(i))
    for i in range(20):
        print(m(i))

main()