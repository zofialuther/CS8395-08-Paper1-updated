class Church:
    def zero():
        return lambda f: lambda x: x

    def next(n):
        return lambda f: lambda x: f(n(f)(x))

    def plus(a):
        return lambda b: lambda f: lambda x: b(f)(a(f)(x))

    def pow(m):
        return lambda n: m(n)

    def mult(a):
        return lambda b: lambda f: lambda x: b(a(f))(x)

    def toChurchNum(n):
        if n <= 0:
            return zero()
        return next(toChurchNum(n - 1))

    def toInt(c):
        counter = [0]

        def funCounter(f):
            counter[0] += 1
            return f

        plus(zero())(c)(funCounter)(lambda x: x)

        return counter[0]

    zero = zero()
    three = next(next(next(zero)))
    four = next(next(next(next(zero))))

    print("3+4=" + str(toInt(plus(three)(four))))  # prints 7
    print("4+3=" + str(toInt(plus(four)(three))))  # prints 7

    print("3*4=" + str(toInt(mult(three)(four))))  # prints 12
    print("4*3=" + str(toInt(mult(four)(three))))  # prints 12

    print("3^4=" + str(toInt(pow(four)(three))))  # prints 81
    print("4^3=" + str(toInt(pow(three)(four))))  # prints 64

    print("  8=" + str(toInt(toChurchNum(8)))  # prints 8