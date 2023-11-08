```python
class SumDigits:
    def sum_digits_long(self, number):
        sum = 0
        while number != 0:
            sum += number % 10
            number = number // 10
        return sum
    
    def sum_digits_big_integer(self, number, base):
        sum = 0
        while number != 0:
            digit = number % base
            sum += digit
            number = number // base
        return sum

    def main(self):
        long_number = 123456789
        hex_number = 0xABCDEF
        big_integer_number = 1234567890123456789012345678901234567890
        
        print(self.sum_digits_long(long_number))
        print(self.sum_digits_big_integer(hex_number, 16))
        print(self.sum_digits_big_integer(big_integer_number, 10))

# Usage
sum_digits = SumDigits()
sum_digits.main()
```