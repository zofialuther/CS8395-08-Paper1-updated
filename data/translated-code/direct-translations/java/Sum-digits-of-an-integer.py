from math import log

def sumDigits(num, base=10):
    if isinstance(num, int):
        s = str(num)
    else:
        s = num.toString(base)
    result = sum(int(digit, base) for digit in s)
    return result

print(sumDigits(1))
print(sumDigits(12345))
print(sumDigits(123045))
print(sumDigits(0xfe, 16))
print(sumDigits(0xf0e, 16))
print(sumDigits(12345678901234567890))