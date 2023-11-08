```python
class RPN:
    @staticmethod
    def main(args):
        RPN.evalRPN("3 4 2 * 1 5 - 2 3 ^ ^ / +")

    @staticmethod
    def evalRPN(expr):
        stack = []
        print("Input\tOperation\tStack after")
        for token in expr.split(" "):
            print(token + "\t", end="")
            if token == "*":
                print("Operate\t\t", end="")
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(firstOperand * secondOperand)
            elif token == "/":
                print("Operate\t\t", end="")
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(firstOperand / secondOperand)
            elif token == "-":
                print("Operate\t\t", end="")
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(firstOperand - secondOperand)
            elif token == "+":
                print("Operate\t\t", end="")
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(firstOperand + secondOperand)
            elif token == "^":
                print("Operate\t\t", end="")
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(pow(firstOperand, secondOperand))
            else:
                print("Push\t\t", end="")
                try:
                    stack.append(float(token))
                except ValueError:
                    print("\nError: invalid token " + token)
                    return
            print(stack)
        if len(stack) > 1:
            print("Error, too many operands: " + str(stack))
            return
        print("Final answer: " + str(stack.pop()))
```