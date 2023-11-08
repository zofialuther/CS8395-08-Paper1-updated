small = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

big = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]

def main():
    print(int2Text(0))
    print(int2Text(10))
    print(int2Text(30))
    print(int2Text(47))
    print(int2Text(100))
    print(int2Text(999))
    print(int2Text(1000))
    print(int2Text(9999))
    print(int2Text(123456))
    print(int2Text(900000001))
    print(int2Text(1234567890))
    print(int2Text(-987654321))
    print(int2Text(9223372036854775807))
    print(int2Text(-9223372036854775808))

def int2Text(number):
    sb = ""

    if number == 0:
        return "zero"
    
    num = abs(number)
    unit = 0

    while True:
        rem100 = num % 100
        if rem100 >= 20:
            if rem100 % 10 == 0:
                sb = tens[rem100 // 10] + " " + sb
            else:
                sb = tens[rem100 // 10] + "-" + small[rem100 % 10] + " " + sb
        elif rem100 != 0:
            sb = small[rem100] + " " + sb

        hundreds = num % 1000 // 100
        if hundreds != 0:
            sb = small[hundreds] + " hundred " + sb

        num = num // 1000
        if num == 0:
            break

        rem1000 = num % 1000
        if rem1000 != 0:
            sb = big[unit] + " " + sb
        unit += 1

    if number < 0:
        sb = "negative " + sb

    return sb.strip()