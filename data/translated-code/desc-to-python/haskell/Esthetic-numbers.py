```python
def is_esthetic_number(num, base):
    digits = convert_to_base(num, base)
    for i in range(len(digits) - 1):
        if abs(digits[i] - digits[i+1]) != 1:
            return False
    return True

def convert_to_base(num, base):
    result = []
    while num > 0:
        result.append(num % base)
        num //= base
    return result[::-1]

def convert_from_base(digits, base):
    result = 0
    for digit in digits:
        result = result * base + digit
    return result

def represent_in_base(num, base):
    return ''.join(str(digit) for digit in convert_to_base(num, base))
```