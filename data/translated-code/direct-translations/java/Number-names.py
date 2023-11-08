```python
class IntToWords:
    small = ["", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    big = ["", "thousand", "million", "billion", "trillion",
           "quadrillion", "quintillion"]

    @staticmethod
    def int2Text(number):
        sb = []

        if number == 0:
            return "zero"

        num = -abs(number)

        unit = 1
        while True:
            rem100 = int(-(num % 100))
            if rem100 >= 20:
                if rem100 % 10 == 0:
                    sb.insert(0, IntToWords.tens[rem100 // 10] + " ")
                else:
                    sb.insert(0, IntToWords.tens[rem100 // 10] + "-" + IntToWords.small[rem100 % 10] + " ")
            elif rem100 != 0:
                sb.insert(0, IntToWords.small[rem100] + " ")

            hundreds = int(-(num % 1000) / 100)
            if hundreds != 0:
                sb.insert(0, IntToWords.small[hundreds] + " hundred ")

            num //= 1000
            if num == 0:
                break

            rem1000 = int(-(num % 1000))
            if rem1000 != 0:
                sb.insert(0, IntToWords.big[unit] + " ")
            unit += 1

        if number < 0:
            sb.insert(0, "negative ")

        return ''.join(sb).strip()


print(IntToWords.int2Text(0))
print(IntToWords.int2Text(10))
print(IntToWords.int2Text(30))
print(IntToWords.int2Text(47))
print(IntToWords.int2Text(100))
print(IntToWords.int2Text(999))
print(IntToWords.int2Text(1000))
print(IntToWords.int2Text(9999))
print(IntToWords.int2Text(123456))
print(IntToWords.int2Text(900000001))
print(IntToWords.int2Text(1234567890))
print(IntToWords.int2Text(-987654321))
```