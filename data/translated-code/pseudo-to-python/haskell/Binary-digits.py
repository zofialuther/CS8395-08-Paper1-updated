```python
def binaryDigits(n):
    result = ""
    while n != 0:
        digit = n % 2
        result = str(digit) + result
        n = n // 2
    return result

def main():
    numbers = [5, 50, 9000]
    for number in numbers:
        digits = binaryDigits(number)
        print(number, "->", digits)
```