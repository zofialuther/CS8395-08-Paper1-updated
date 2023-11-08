import math

class ArithmeticEvaluation:

    class Expression:
        def eval(self):
            pass

    class Parentheses:
        LEFT = ''

    class BinaryOperator:
        def __init__(self, symbol, precedence):
            self.symbol = symbol
            self.precedence = precedence

        def eval(self, leftValue, rightValue):
            pass

        def forSymbol(symbol):
            pass

    class Number(Expression):
        def __init__(self, number):
            self.number = number

        def eval(self):
            return self.number

        def __str__(self):
            return str(self.number)

    class BinaryExpression(Expression):
        def __init__(self, leftOperand, operator, rightOperand):
            self.leftOperand = leftOperand
            self.operator = operator
            self.rightOperand = rightOperand

        def eval(self):
            leftValue = self.leftOperand.eval()
            rightValue = self.rightOperand.eval()
            return self.operator.eval(leftValue, rightValue)

        def __str__(self):
            return "(" + str(self.leftOperand) + " " + self.operator.symbol + " " + str(self.rightOperand) + ")"

    def createNewOperand(operator, operands):
        rightOperand = operands.pop()
        leftOperand = operands.pop()
        operands.append(ArithmeticEvaluation.BinaryExpression(leftOperand, operator, rightOperand))

    def parse(input):
        curIndex = 0
        afterOperand = False
        operands = []
        operators = []
        while curIndex < len(input):
            startIndex = curIndex
            c = input[curIndex]
            curIndex += 1

            if c.isspace():
                continue

            if afterOperand:
                if c == ')':
                    operator = operators.pop()
                    while operators and operator != ArithmeticEvaluation.Parentheses.LEFT:
                        createNewOperand(operator, operands)
                    continue
                afterOperand = False
                operator = ArithmeticEvaluation.BinaryOperator.forSymbol(c)
                while operators and operators[-1] != ArithmeticEvaluation.Parentheses.LEFT and operators[-1].precedence >= operator.precedence:
                    createNewOperand(operators.pop(), operands)
                operators.append(operator)
                continue

            if c == '(':
                operators.append(ArithmeticEvaluation.Parentheses.LEFT)
                continue

            afterOperand = True
            while curIndex < len(input):
                c = input[curIndex]
                if not (c.isdigit() or c == '.'):
                    break
                curIndex += 1
            operands.append(ArithmeticEvaluation.Number(int(input[startIndex:curIndex])))

        while operators:
            operator = operators.pop()
            if operator == ArithmeticEvaluation.Parentheses.LEFT:
                raise ValueError
            createNewOperand(operator, operands)

        expression = operands.pop()
        if operands:
            raise ValueError
        return expression

    def main():
        testExpressions = [
            "2+3",
            "2+3/4",
            "2*3-4",
            "2*(3+4)+5/6",
            "2 * (3 + (4 * 5 + (6 * 7) * 8) - 9) * 10",
            "2*-3--4+-.25"
        ]
        for testExpression in testExpressions:
            expression = parse(testExpression)
            print(f"Input: \"{testExpression}\", AST: \"{expression}\", value={expression.eval()}")

ArithmeticEvaluation.main()