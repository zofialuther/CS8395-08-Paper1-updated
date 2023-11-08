```python
import random

class Game24:
    r = random

    def main():
        digits = Game24.randomDigits()
        print("Make 24 using these digits: ", digits)
        print("> ")
        s = []
        total = 0
        userInput = input()
        for char in userInput:
            if char.isdigit():
                total += int(char)
                s.append(float(char))
            elif char in ['+', '-', '*', '/']:
                b = s.pop()
                a = s.pop()
                result = Game24.applyOperator(a, b, char)
                s.append(result)
        if total != Game24.tallyDigits(digits):
            print("Not the same digits.")
        elif abs(24 - s[-1]) < 0.001:
            print("Correct!")
        else:
            print("Not correct.")

    @staticmethod
    def applyOperator(a, b, c):
        if c == '+':
            return a + b
        elif c == '-':
            return b - a
        elif c == '*':
            return a * b
        elif c == '/':
            return b / a
        else:
            return float('nan')

    @staticmethod
    def tallyDigits(a):
        total = 0
        for i in range(4):
            total += (1 << (a[i] * 5))
        return total

    @staticmethod
    def randomDigits():
        result = [Game24.r.randint(1, 9) for _ in range(4)]
        return result
```