```python
class Complex(complex):
    def is_purely_imaginary(self):
        return self.real == 0
    
    def is_purely_real(self):
        return self.imag == 0
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
def croots(n):
    return [Complex(cmath.rect(1, 2 * k * cmath.pi / n)) for k in range(n)]

for i in range(2, 11):
    print(f"Roots of unity for n={i}: {croots(i)}")
```