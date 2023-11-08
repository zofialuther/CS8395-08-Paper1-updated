def except(numer, denom):
    try:
        dummy = int(numer) / int(denom) # ArithmeticException is only thrown from integer math
        return False
    except ArithmeticError:
        return True