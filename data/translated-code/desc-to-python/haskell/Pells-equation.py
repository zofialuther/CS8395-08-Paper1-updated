def pell(n):
    def go(a, b, k):
        if k == 0:
            return (a, b)
        else:
            return go(a + 2 * b, a + b, k - 1)
    return go(0, 1, n)