from enum import Enum

class ArithmeticEvaluation:
  
  class BinaryOperator(Enum):
    ADD = ('+', 1)
    SUB = ('-', 1)
    MUL = ('*', 2)
    DIV = ('/', 2)
    
    def eval(self, leftValue, rightValue):
      if self == self.ADD:
        return leftValue + rightValue
      elif self == self.SUB:
        return leftValue - rightValue
      elif self == self.MUL:
        return leftValue * rightValue
      elif self == self.DIV:
        return leftValue / rightValue
      else:
        raise RuntimeError("Invalid operator")
  
  class Number:
    def __init__(self, number):
      self.number = number
    
    def eval(self):
      return self.number
    
    def __str__(self):
      return str(self.number)
  
  class BinaryExpression:
    def __init__(self, leftOperand, operator, rightOperand):
      self.leftOperand = leftOperand
      self.operator = operator
      self.rightOperand = rightOperand
    
    def eval(self):
      leftValue = self.leftOperand.eval()
      rightValue = self.rightOperand.eval()
      return self.operator.eval(leftValue, rightValue)
    
    def __str__(self):
      return "(" + str(self.leftOperand) + " " + self.operator.value[0] + " " + str(self.rightOperand) + ")"
  
  def createNewOperand(operator, operands):
    rightOperand = operands.pop()
    leftOperand = operands.pop()
    operands.append(BinaryExpression(leftOperand, operator, rightOperand))
  
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
          while operators and operator != '(':
            createNewOperand(operator, operands)
          continue
        afterOperand = False
        operator = None
        for op in BinaryOperator:
          if op.value[0] == c:
            operator = op
            break
        if operator is None:
          raise ValueError("Invalid operator")
        while operators and operators[-1] != '(' and operators[-1].value[1] >= operator.value[1]:
          createNewOperand(operators.pop(), operands)
        operators.append(operator)
        continue
      
      if c == '(':
        operators.append('(')
        continue
      
      afterOperand = True
      while curIndex < len(input):
        c = input[curIndex]
        if not c.isdigit() and c != '.':
          break
        curIndex += 1
      operands.append(Number(float(input[startIndex:curIndex])))
    
    while operators:
      operator = operators.pop()
      if operator == '(':
        raise ValueError("Unmatched parentheses")
      createNewOperand(operator, operands)
    
    expression = operands.pop()
    if operands:
      raise ValueError("Invalid input")
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
      print("Input: \"" + testExpression + "\", AST: \"" + str(expression) + "\", value=" + str(expression.eval()))

ArithmeticEvaluation.main()