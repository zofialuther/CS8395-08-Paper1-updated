```python
import math

def sum_of_squares(Xs, Sum):
    if not Xs:
        return Sum
    else:
        return sum_of_squares(Xs[1:], Sum + Xs[0] * Xs[0])

def rms(Xs):
    Sum = sum_of_squares(Xs, 0)
    N = len(Xs)
    return math.sqrt(Sum / N)

if __name__ == "__main__":
    Xs = list(range(1, 11))
    Y = rms(Xs)
    print(f"The root-mean-square of 1..10 is {Y}")
```