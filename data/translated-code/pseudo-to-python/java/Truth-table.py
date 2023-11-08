class TruthTable:
    def __init__(self, symbols):
        variables = set()
        for symbol in symbols:
            if symbol not in operators:
                variables.add(symbol)
        self.variables = list(variables)
        self.symbols = symbols

    def __str__(self):
        result = ''
        for variable in self.variables:
            result += variable + ' '
        result += ' '
        for symbol in self.symbols:
            result += symbol + ' '
        result += '\n'
        for values in enumerate(len(self.variables)):
            i = iter(self.variables)
            for value in values:
                result += f"{i.__next__():{len(i.__next__())}} "
            result += ' '
            result += 'T' if self.evaluate(values) else 'F'
            result += '\n'
        return result

    def enumerate(self, size):
        if size == 1:
            return [[False], [True]]
        return [[False] + head for head in self.enumerate(size - 1)] + [[True] + head for head in self.enumerate(size - 1)]

    def evaluate(self, enumeration):
        values = {}
        stack = []
        for variable, value in zip(self.variables, enumeration):
            values[variable] = value
        for symbol in self.symbols:
            op = operators.get(symbol)
            stack.append(values[symbol]) if op is None else stack.append(op.evaluate(stack))
        return stack.pop()

class Operator:
    def evaluate(self, s):
        pass

operators = {}
operators["&"] = lambda stack: bool(stack.pop() and stack.pop())
operators["|"] = lambda stack: bool(stack.pop() or stack.pop())
operators["!"] = lambda stack: not stack.pop()
operators["^"] = lambda stack: not stack.pop() == stack.pop()

print(TruthTable(symbols))