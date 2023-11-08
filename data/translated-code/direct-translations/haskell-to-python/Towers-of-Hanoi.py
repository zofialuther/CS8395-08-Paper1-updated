def hanoiIO(n):
    def f(t):
        x, y = t
        print("Move " + str(x) + " to " + str(y))

    hanoi(n, 1, 2, 3, f)