```python
class TruthTable:
    def __init__(self, *symbols):
        variables = set()
        for symbol in symbols:
            if symbol not in operators:
                variables.add(symbol)
        self.variables = list(variables)
        self.symbols = symbols

    def __str__(self):
        result = ""
        for variable in self.variables:
            result += variable + " "
        result += " "
        for symbol in self.symbols:
            result += symbol + " "
        result += "\n"
        for values in self.enumerate(len(self.variables)):
            i = iter(self.variables)
            for value in values:
                result += "{:<{}c} ".format('T' if value else 'F', len(next(i)))
            result += " " + ('T' if self.evaluate(values) else 'F') + "\n"
        return result

    @staticmethod
    def enumerate(size):
        if size == 1:
            return [[False], [True]]
        result = []
        for head in TruthTable.enumerate(size - 1):
            result.append(head + [False])
            result.append(head + [True])
        return result

    def evaluate(self, enumeration):
        values = dict(zip(self.variables, enumeration))
        stack = []
        for symbol in self.symbols:
            if symbol in operators:
                stack.append(operators[symbol](stack))
            else:
                stack.append(values[symbol])
        return stack.pop()


operators = {
    "&": lambda stack: stack.pop() and stack.pop(),
    "|": lambda stack: stack.pop() or stack.pop(),
    "!": lambda stack: not stack.pop(),
    "^": lambda stack: stack.pop() != stack.pop()
}

if __name__ == "__main__":
    print(TruthTable("A", "B", "&", "!"))
```