def perform_integer_division(num1, num2):
    try:
        result = num1 // num2
        return False
    except ArithmeticError:
        return True