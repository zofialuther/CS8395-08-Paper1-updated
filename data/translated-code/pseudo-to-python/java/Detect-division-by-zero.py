def except(numer, denom):
    try:
        dummy = int(numer) / int(denom)
        return False
    except ArithmeticError:
        return True