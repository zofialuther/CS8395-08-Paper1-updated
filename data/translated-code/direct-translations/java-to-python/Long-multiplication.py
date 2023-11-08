```python
class LongMultBinary:
    class MyLongNum:
        def __init__(self, value):
            self.digits = [0] * (len(value) // 9 + 1)
            self.digitsUsed = 0
            for i in range(0, len(value), 9):
                chunk = value[i:min(i+9, len(value))]
                multiplier = 1
                addend = 0
                for j in range(len(chunk)):
                    c = chunk[j]
                    if not c.isdigit():
                        raise ValueError(f"Invalid digit {c} found in input")
                    multiplier *= 10
                    addend *= 10
                    addend += int(c)
                self.multiply(multiplier)
                self.add(addend)

        def clone(self):
            clone = LongMultBinary.MyLongNum('')
            clone.digits = self.digits.copy()
            clone.digitsUsed = self.digitsUsed
            return clone

        def resize(self, new_length):
            if len(self.digits) < new_length:
                self.digits += [0] * (new_length - len(self.digits))

        def adjust_digits_used(self):
            while self.digitsUsed > 0 and self.digits[self.digitsUsed - 1] == 0:
                self.digitsUsed -= 1

        def multiply(self, multiplier):
            if multiplier < 0:
                raise ValueError("Signed arithmetic isn't supported")
            self.resize(self.digitsUsed + 1)
            temp = 0
            for i in range(self.digitsUsed):
                temp += (self.digits[i] & 0xFFFFFFFF) * multiplier
                self.digits[i] = temp & 0xFFFFFFFF  # store the low 32 bits
                temp >>= 32
            self.digits[self.digitsUsed] = temp & 0xFFFFFFFF
            self.digitsUsed += 1
            self.adjust_digits_used()

        def add(self, addend):
            if addend < 0:
                raise ValueError("Signed arithmetic isn't supported")
            temp = addend
            for i in range(self.digitsUsed):
                if temp == 0:
                    break
                temp += self.digits[i] & 0xFFFFFFFF
                self.digits[i] = temp & 0xFFFFFFFF  # store the low 32 bits
                temp >>= 32
            if temp != 0:
                self.resize(self.digitsUsed + 1)
                self.digits[self.digitsUsed] = temp & 0xFFFFFFFF
                self.digitsUsed += 1

        def divide(self, divisor):
            if divisor < 0:
                raise ValueError("Signed arithmetic isn't supported")
            remainder = 0
            for i in range(self.digitsUsed - 1, -1, -1):
                two_digits = (remainder << 32) | (self.digits[i] & 0xFFFFFFFF)
                remainder = two_digits % divisor
                self.digits[i] = two_digits // divisor
            self.adjust_digits_used()
            return remainder

        def __str__(self):
            if self.digitsUsed == 0:
                return "0"
            dummy = self.clone()
            result_builder = []
            while dummy.digitsUsed > 0:
                decimal_digits = dummy.divide(1000000000)
                for _ in range(9):
                    result_builder.append(chr(decimal_digits % 10 + ord('0')))
                    decimal_digits //= 10
            while result_builder[-1] == '0':
                result_builder.pop()
            return ''.join(result_builder[::-1])

        def multiply(self, multiplier):
            left, right = (self, multiplier) if self.digitsUsed > multiplier.digitsUsed else (multiplier, self)
            new_digits = [0] * (left.digitsUsed + right.digitsUsed)
            for right_pos in range(right.digitsUsed):
                right_digit = right.digits[right_pos] & 0xFFFFFFFF
                temp = 0
                for left_pos in range(left.digitsUsed):
                    temp += new_digits[left_pos + right_pos] & 0xFFFFFFFF
                    temp += right_digit * (left.digits[left_pos] & 0xFFFFFFFF)
                    new_digits[left_pos + right_pos] = temp & 0xFFFFFFFF
                    temp >>= 32
                dest_pos = right_pos + self.digitsUsed
                while temp != 0:
                    temp += new_digits[dest_pos] & 0xFFFFFFFF
                    new_digits[dest_pos] = temp & 0xFFFFFFFF
                    temp >>= 32
                    dest_pos += 1
            self.digits = new_digits
            self.digitsUsed = len(new_digits)
            self.adjust_digits_used()

    def main(self):
        one = self.MyLongNum("18446744073709551616")
        two = one.clone()
        one.multiply(two)
        print(one)


LongMultBinary().main()
```