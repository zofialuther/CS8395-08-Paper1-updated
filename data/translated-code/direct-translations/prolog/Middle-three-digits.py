def middle_3_digits(Number, D):
    Digits = []
    verify_middle_3_able(Number, Digits)
    FrontDigits = Digits[:len(Digits)//2]
    BackDigits = Digits[len(Digits)//2:]
    if D == [FrontDigits[-1], FrontDigits[-2], FrontDigits[-3]]:
        return True
    else:
        return False

def verify_middle_3_able(Number, Digits):
    if not isinstance(Number, int):
        raise TypeError('Number must be an integer')
    AbsNumber = abs(Number)
    Digits = [int(x) for x in str(AbsNumber)]
    NumDigits = len(Digits)
    if NumDigits < 3:
        raise ValueError('Number must have at least 3 digits')
    elif NumDigits % 2 == 0:
        raise ValueError('Number must have an odd number of digits')
    else:
        return True