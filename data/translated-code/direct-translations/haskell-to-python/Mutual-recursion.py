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

if __name__ == "__main__":
    print(list(map(f, range(20))))
    print(list(map(m, range(20))))