```python
import math

class RootMeanSquare:
    def rootMeanSquare(self, *args):
        sum_of_squares = sum(x ** 2 for x in args)
        mean_of_squares = sum_of_squares / len(args)
        root_mean_square = math.sqrt(mean_of_squares)
        return root_mean_square

if __name__ == "__main__":
    rms = RootMeanSquare()
    numbers = list(range(1, 11))
    result = rms.rootMeanSquare(*numbers)
    print(result)
```