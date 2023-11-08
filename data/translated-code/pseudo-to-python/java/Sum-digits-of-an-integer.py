def sumDigits(num):
    return sumDigitsHelper(num, 10)

def sumDigitsHelper(num, base):
    s = str(num)
    result = 0
    for i in range(len(s)):
        result = result + int(s[i], base)
    return result

def main():
    print(sumDigits(1))
    print(sumDigits(12345))
    print(sumDigits(123045))
    print(sumDigits(0xfe, 16))
    print(sumDigits(0xf0e, 16))
    print(sumDigits(12345678901234567890))

main()