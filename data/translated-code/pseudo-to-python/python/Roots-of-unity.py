```python
import cmath

class Complex(complex):
    def __repr__(self):
        return f"{self.real} + {self.imag}i"
    
    def pureImag(self):
        return abs(self.real) < 0.0001
    
    def pureReal(self):
        return abs(self.imag) < 0.0001

def croots(n):
    if n <= 0:
        return None
    return (cmath.rect(1, 2 * k * cmath.pi / n) for k in range(n))

for i in range(2, 11):
    print(f"Number: {i}")
    print(list(croots(i)))
```