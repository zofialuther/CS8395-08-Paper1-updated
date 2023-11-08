class MutualRecursion:
    def main(arr):
        max = 20
        print("First %d values of the Female sequence:  %n", max)
        for i in range(0, max+1):
            print("  f(%d) = %d%n", i, f(i))
        print("First %d values of the Male sequence:  %n", max)
        for i in range(0, max+1):
            print("  m(%d) = %d%n", i, m(i))

    F_MAP = {}
    def f(n):
        if n in F_MAP:
            return F_MAP[n]
        fn = 1 if n == 0 else n - m(f(n - 1))
        F_MAP[n] = fn
        return fn

    M_MAP = {}
    def m(n):
        if n in M_MAP:
            return M_MAP[n]
        mn = 0 if n == 0 else n - f(m(n - 1))
        M_MAP[n] = mn
        return mn