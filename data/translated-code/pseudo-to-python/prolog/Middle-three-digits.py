```python
def middle_3_digits(Number, [D1,D2,D3]):
    verify_middle_3_able(Number, [D1,D2,D3])
    Digits = list(str(abs(Number)))
    FrontDigits = Digits[:len(Digits)//2]
    BackDigits = Digits[len(Digits)//2:]
    if len(FrontDigits) != len(BackDigits):
        return False
    return [D1,D2,D3] == BackDigits[:3]

def verify_middle_3_able(Number, Digits):
    if type(Number) != int and type(Number) != float:
        raise TypeError("Number must be a number")
    AbsNumber = abs(Number)
    Digits = list(str(AbsNumber))
    NumDigits = len(Digits)
    if 3 > NumDigits:
        raise ValueError("Number must have at least 3 digits")
    if NumDigits % 2 == 0:
        raise ValueError("Number must have an odd number of digits")
```