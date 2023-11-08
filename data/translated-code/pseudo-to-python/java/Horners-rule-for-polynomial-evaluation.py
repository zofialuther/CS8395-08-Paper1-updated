```python
class Horner:
    def main(self):
        coeffs = []
        coeffs.append(-19.0)
        coeffs.append(7.0)
        coeffs.append(-4.0)
        coeffs.append(6.0)
        print(self.polyEval(coeffs, 3))
        
    def polyEval(self, coefficients, x):
        coefficients.reverse()
        accumulator = coefficients[0]
        for i in range(1, len(coefficients)):
            accumulator = accumulator * x + coefficients[i]
        return accumulator

h = Horner()
h.main()
```