```python
import re

class Fractran:
    def __init__(self, program, value):
        self.program = program
        self.value = value
        self.numerator = []
        self.denominator = []

    def compile_program(self):
        fractions = re.findall(r'\d+/\d+', self.program)
        for fraction in fractions:
            num, denom = fraction.split('/')
            self.numerator.append(int(num))
            self.denominator.append(int(denom))

    def step(self):
        for i in range(len(self.numerator)):
            if self.value % self.denominator[i] == 0:
                self.value = (self.value * self.numerator[i]) // self.denominator[i]
                print(self.value)
                break

    def run(self, limit):
        for _ in range(limit):
            self.step()

    def dump(self):
        print(f"Numerator: {self.numerator}")
        print(f"Denominator: {self.denominator}")

program = "2/3 3/4"
value = 2
frac = Fractran(program, value)
frac.compile_program()
frac.run(10)
frac.dump()
```