```python
class Horner:
    def main(args):
        coeffs = [-19.0, 7.0, -4.0, 6.0]
        print(polyEval(coeffs, 3))
    
    def polyEval(coefficients, x):
        coefficients = coefficients[::-1]
        accumulator = coefficients[0]
        for i in range(1, len(coefficients)):
            accumulator = (accumulator * x) + coefficients[i]
        return accumulator
```