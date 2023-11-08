from typing import TypeVar, Callable

OUTPUT = TypeVar('OUTPUT')
INPUT = TypeVar('INPUT')

class SelfApplicable:
    def apply(self, input: 'SelfApplicable[OUTPUT]') -> OUTPUT:
        pass

class Utils:
    @staticmethod
    def y() -> 'SelfApplicable[Callable[Callable[Callable[INPUT, OUTPUT], Callable[INPUT, OUTPUT]], Callable[INPUT, OUTPUT]]]':
        return lambda y: lambda f: lambda x: f(y(y)(f))(x)

    @staticmethod
    def fix() -> Callable[Callable[Callable[INPUT, OUTPUT], Callable[INPUT, OUTPUT]], Callable[INPUT, OUTPUT]]:
        return Utils.y()(Utils.y())

    @staticmethod
    def fib(m: int) -> int:
        if m < 0:
            raise ValueError("n can not be a negative number")

        return Utils.fix()(lambda f: lambda n: n if n < 2 else f(n - 1) + f(n - 2))(m)