def evalRPN(expr):
    stack = []
    print("Input\tOperation\tStack after")
    for token in expr.split("\\s"):
        print(token + "\t")
        if token == "*":
            print("Operate\t\t")
            secondOperand = stack.pop()
            firstOperand = stack.pop()
            stack.append(firstOperand * secondOperand)
        elif token == "/":
            print("Operate\t\t")
            secondOperand = stack.pop()
            firstOperand = stack.pop()
            stack.append(firstOperand / secondOperand)
        elif token == "-":
            print("Operate\t\t")
            secondOperand = stack.pop()
            firstOperand = stack.pop()
            stack.append(firstOperand - secondOperand)
        elif token == "+":
            print("Operate\t\t")
            secondOperand = stack.pop()
            firstOperand = stack.pop()
            stack.append(firstOperand + secondOperand)
        elif token == "^":
            print("Operate\t\t")
            secondOperand = stack.pop()
            firstOperand = stack.pop()
            stack.append(pow(firstOperand, secondOperand))
        else:
            print("Push\t\t")
            try:
                stack.append(float(token))
            except ValueError:
                print("Error: invalid token " + token)
                return
        print(stack)
    if len(stack) > 1:
        print("Error, too many operands: " + stack)
        return
    print("Final answer: " + str(stack.pop()))