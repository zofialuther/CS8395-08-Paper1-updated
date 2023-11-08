```python
class MinimumMultipleDigitSum:
    @staticmethod
    def main(aArgs):
        for n in range(1, 71):
            k = 0
            while MinimumMultipleDigitSum.digitSum(k + n) != n:
                k += n
            print(f"{k // n:8d}" + ("\n" if n % 10 == 0 else " "), end="")

    @staticmethod
    def digitSum(aN):
        sum = 0
        while aN > 0:
            sum += aN % 10
            aN //= 10
        return sum
```