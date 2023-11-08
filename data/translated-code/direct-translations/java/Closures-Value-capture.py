from typing import List
from functools import reduce

class ValueCapture:
    @staticmethod
    def main(*arguments):
        closures: List[IntSupplier] = list(map(lambda i: lambda: i * i, range(0, 11)))

        closure: IntSupplier = closures[3]
        print(closure())  # prints "9"