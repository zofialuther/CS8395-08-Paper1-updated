```python
class Mult:
    def __init__(self):
        self.results = {}

    def double_num(self, num):
        return num * 2

    def halve_num(self, num):
        return num / 2

    def is_even(self, num):
        return num % 2 == 0

    def main(self):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if self.is_even(num1):
            self.results['double_num1'] = self.double_num(num1)
        else:
            self.results['halve_num1'] = self.halve_num(num1)

        if self.is_even(num2):
            self.results['double_num2'] = self.double_num(num2)
        else:
            self.results['halve_num2'] = self.halve_num(num2)

        print("Final results:", self.results)
        print("Sum of final values:", sum(self.results.values()))

Mult().main()
```