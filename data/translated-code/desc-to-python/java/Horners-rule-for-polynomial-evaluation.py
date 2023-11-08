```python
class Horner:
    def polyEval(self, coefficients, x):
        result = coefficients[0]
        for i in range(1, len(coefficients)):
            result = result * x + coefficients[i]
        return result

if __name__ == "__main__":
    coefficients = [2, -1, 3, -2]
    x = 2
    horner = Horner()
    print(horner.polyEval(coefficients, x))
```