def div_check(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return True
    else:
        return False