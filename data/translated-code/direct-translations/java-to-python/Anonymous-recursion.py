from typing import Callable

class SelfApplicable:
    def apply(self, input: 'SelfApplicable') -> 'SelfApplicable':
        pass

class Utils:
    @staticmethod
    def y() -> Callable[[Callable[[Callable], Callable]], Callable]:
        def inner(y):
            def inner2(f):
                def inner3(x):
                    return f(y(y)(f))(x)
                return inner3
            return inner2
        return inner

    @staticmethod
    def fix() -> Callable[[Callable[[Callable], Callable]], Callable]:
        return Utils.y()(Utils.y())

    @staticmethod
    def fib(m: int) -> int:
        if m < 0:
            raise ValueError("n can not be a negative number")

        return Utils.fix()(lambda f: lambda n: n if n < 2 else f(n - 1) + f(n - 2))(m)