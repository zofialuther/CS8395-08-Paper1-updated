def repeat(n, fun):
    for i in range(n):
        fun(i + 1)

repeat(3, lambda x: print("Example " + str(x)))