```python
import math
import decimal

class Pi:
    def __init__(self):
        self.a = decimal.Decimal(1)
        self.b = decimal.Decimal(1) / decimal.Decimal(math.sqrt(2))
        self.t = decimal.Decimal(1) / decimal.Decimal(4)
        self.p = decimal.Decimal(1)

    def calcPiDigits(self):
        while True:
            a_next = (self.a + self.b) / decimal.Decimal(2)
            b_next = decimal.Decimal(math.sqrt(self.a * self.b))
            t_next = self.t - self.p * (self.a - a_next) * (self.a - a_next)
            p_next = decimal.Decimal(2) * self.p

            pi_approximation = (a_next + b_next) * (a_next + b_next) / (decimal.Decimal(4) * t_next)

            print(pi_approximation)

            self.a = a_next
            self.b = b_next
            self.t = t_next
            self.p = p_next

pi = Pi()
pi.calcPiDigits()
```