```python
class DotProduct:
    def main(self):
        a = [1, 3, -5]
        b = [4, -2, -1]
        print(self.dotProd(a, b))

    def dotProd(self, a, b):
        if len(a) != len(b):
            raise ValueError("The dimensions have to be equal!")
        sum = 0
        for i in range(len(a)):
            sum += a[i] * b[i]
        return sum

dp = DotProduct()
dp.main()
```