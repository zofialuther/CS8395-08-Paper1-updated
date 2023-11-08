```python
def uniqueDigits(num):
    digit_set = set(str(num))
    return len(digit_set) == len(str(num)) and '0' not in digit_set and '5' not in digit_set

def testNumber(num):
    for digit in str(num):
        if int(digit) == 0 or int(digit) == 5:
            continue
        if num % int(digit) != 0:
            return False
    return True

def main():
    num = 98764321
    while num > 0:
        if uniqueDigits(num) and testNumber(num):
            print(num)
            break
        num -= 1

main()
```