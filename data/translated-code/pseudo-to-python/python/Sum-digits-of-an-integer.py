def sumDigits(num, base=10):
    if base < 2:
        print("Error: base must be at least 2")
        return
    num = abs(num)
    sum = 0
    while num >= base:
        num, rem = divmod(num, base)
        sum = sum + rem
    return sum + num

print(sumDigits(1))
print(sumDigits(12345))
print(sumDigits(-123045))
print(sumDigits(0xfe, 16))
print(sumDigits(0xf0e, 16))