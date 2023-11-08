```python
from typing import Callable

class Church:
    ChurchNum = Callable[[Callable], Callable]

    @staticmethod
    def zero() -> ChurchNum:
        return lambda f: lambda x: x

    @staticmethod
    def next(n: ChurchNum) -> ChurchNum:
        return lambda f: lambda x: f(n(f)(x))

    @staticmethod
    def plus(a: ChurchNum) -> ChurchNum:
        return lambda b: lambda f: lambda x: b(f)(a(f)(x))

    @staticmethod
    def pow(m: ChurchNum) -> ChurchNum:
        return lambda n: m(n)

    @staticmethod
    def mult(a: ChurchNum) -> ChurchNum:
        return lambda b: lambda f: lambda x: b(a(f))(x)

    @staticmethod
    def toChurchNum(n: int) -> ChurchNum:
        if n <= 0:
            return Church.zero()
        return Church.next(Church.toChurchNum(n - 1))

    @staticmethod
    def toInt(c: ChurchNum) -> int:
        counter = 0
        def funCounter(f):
            nonlocal counter
            counter += 1
            return f
        Church.plus(Church.zero())(c)(funCounter)(lambda x: x)
        return counter

    @staticmethod
    def main():
        zero = Church.zero()
        three = Church.next(Church.next(Church.next(zero)))
        four = Church.next(Church.next(Church.next(Church.next(zero))))

        print("3+4=" + str(Church.toInt(Church.plus(three)(four))))  # prints 7
        print("4+3=" + str(Church.toInt(Church.plus(four)(three))))  # prints 7
        print("3*4=" + str(Church.toInt(Church.mult(three)(four))))  # prints 12
        print("4*3=" + str(Church.toInt(Church.mult(four)(three))))  # prints 12
        print("3^4=" + str(Church.toInt(Church.pow(four)(three))))  # prints 81
        print("4^3=" + str(Church.toInt(Church.pow(three)(four))))  # prints 64
        print("  8=" + str(Church.toInt(Church.toChurchNum(8))))     # prints 8

Church.main()
```