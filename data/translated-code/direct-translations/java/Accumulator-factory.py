from typing import Union
from numbers import Number

class AccumulatorFactory:
    @staticmethod
    def accumulator(sum0: Number) -> UnaryOperator[Number]:
        # Allows sum[0] = ... inside lambda.
        sum = [sum0]

        # Acts like n -> sum[0] += n, but chooses long or double.
        # Converts weird types (like BigInteger) to double.
        def accumulator_func(n: Number) -> Union[int, float]:
            if AccumulatorFactory.longable(sum[0]) and AccumulatorFactory.longable(n):
                sum[0] = sum[0].longValue() + n.longValue()
            else:
                sum[0] = sum[0].doubleValue() + n.doubleValue()
            return sum[0]

        return accumulator_func

    @staticmethod
    def longable(n: Number) -> bool:
        return isinstance(n, (int, float))

if __name__ == "__main__":
    x = AccumulatorFactory.accumulator(1)
    x(5)
    AccumulatorFactory.accumulator(3)
    print(x(2.3))