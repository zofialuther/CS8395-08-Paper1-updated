def digsum(base):
    def f(a, n):
        if n == 0:
            return a
        else:
            q, r = divmod(n, base)
            return f(a + r, q)
    return f(0, base)

def main():
    print(digsum(16, 255)) # "FF": 15 + 15 = 30

if __name__ == "__main__":
    main()