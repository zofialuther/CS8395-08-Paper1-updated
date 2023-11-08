# Python code
def happy(number):
    m = 0
    digit = 0
    cycle = set()
    while number != 1 and number not in cycle:
        m = 0
        while number > 0:
            digit = number % 10
            m += digit * digit
            number //= 10
        number = m
    return number == 1

count = 0
num = 1
while count < 8:
    if happy(num):
        print(num)
        count += 1
    num += 1