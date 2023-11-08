```python
class Function:
    def apply(self, x):
        pass

class FirstClass:
    @staticmethod
    def compose(f, g):
        def inner(x):
            return f.apply(g.apply(x))
        return inner

    @staticmethod
    def main(args):
        functions = []

        class CosFunction(Function):
            def apply(self, x):
                return math.cos(x)
        functions.append(CosFunction())

        class TanFunction(Function):
            def apply(self, x):
                return math.tan(x)
        functions.append(TanFunction())

        class SquareFunction(Function):
            def apply(self, x):
                return x * x
        functions.append(SquareFunction())

        inverse = []

        class AcosFunction(Function):
            def apply(self, x):
                return math.acos(x)
        inverse.append(AcosFunction())

        class AtanFunction(Function):
            def apply(self, x):
                return math.atan(x)
        inverse.append(AtanFunction())

        class SqrtFunction(Function):
            def apply(self, x):
                return math.sqrt(x)
        inverse.append(SqrtFunction())

        print("Compositions:")
        for i in range(len(functions)):
            print(FirstClass.compose(functions[i], inverse[i]).apply(0.5))

        print("Hard-coded compositions:")
        print(math.cos(math.acos(0.5)))
        print(math.tan(math.atan(0.5)))
        print(math.sqrt(0.5) ** 2)
```