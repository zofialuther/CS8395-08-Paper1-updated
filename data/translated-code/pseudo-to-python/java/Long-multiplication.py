```python
import copy

class LongMultBinary:
    
    class MyLongNum:
        
        def __init__(self, value):
            self.digits = [int(x) for x in value]
            self.digitsUsed = len(value)
        
        def clone(self):
            return copy.deepcopy(self)
        
        def resize(self, newSize):
            self.digits = self.digits + [0]*(newSize - self.digitsUsed)
        
        def adjustDigitsUsed(self, newSize):
            self.digitsUsed = newSize
        
        def multiply(self, digit):
            carry = 0
            for i in range(self.digitsUsed):
                product = self.digits[i] * digit + carry
                self.digits[i] = product % 2
                carry = product // 2
            if carry > 0:
                self.digits.append(carry)
                self.digitsUsed += 1
        
        def add(self, digit):
            carry = digit
            for i in range(self.digitsUsed):
                sum = self.digits[i] + carry
                self.digits[i] = sum % 2
                carry = sum // 2
            if carry > 0:
                self.digits.append(carry)
                self.digitsUsed += 1
        
        def divide(self, digit):
            remainder = 0
            for i in range(self.digitsUsed - 1, -1, -1):
                current = self.digits[i] + remainder*2
                self.digits[i] = current // digit
                remainder = current % digit
        
        def toString(self):
            return ''.join(map(str, self.digits))
    
    def multiply(self, num1, num2):
        result = self.MyLongNum("0")
        for i in range(num2.digitsUsed - 1, -1, -1):
            temp = num1.clone()
            for j in range(num2.digits[num2.digitsUsed - i - 1]):
                result.add(int(temp.toString(), 2))
            result.resize(result.digitsUsed + 1)
            num1.resize(num1.digitsUsed + 1)
            num1.digits = [0] + num1.digits
        return result.toString()

if __name__ == "__main__":
    lm = LongMultBinary()
    num1 = lm.MyLongNum("101")
    num2 = lm.MyLongNum("110")
    result = lm.multiply(num1, num2)
    print(result)
```