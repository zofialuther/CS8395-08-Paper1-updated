def digsum(base, n):
    def f(n, acc):
        if n == 0:
            return acc
        else:
            return f(n//base, acc + n%base)
    return f(n, 0)

print(digsum(16, 255)) # Output: "FF" and 30