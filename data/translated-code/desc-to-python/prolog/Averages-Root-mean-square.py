```python
import math

def sum_of_squares(Xs, Result):
    if not Xs:
        return Result
    else:
        head = Xs[0]
        tail = Xs[1:]
        Result += head**2
        return sum_of_squares(tail, Result)

def rms(Xs, Result):
    SumOfSquares = sum_of_squares(Xs, 0)
    Result = math.sqrt(SumOfSquares/len(Xs))
    return Result

def main():
    Xs = list(range(1, 11))
    result = rms(Xs, 0)
    print(result)

main()
```