def div_check(x, y):
    try:
        result = x / y
        return False
    except ZeroDivisionError:
        return True