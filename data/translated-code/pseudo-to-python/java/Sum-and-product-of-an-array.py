from java.util import Arrays

class SumProd:
    def main(self, arr):
        arg = [1, 2, 3, 4, 5]
        print(Arrays.stream(arg).sum())
        print(Arrays.stream(arg).reduce(0, lambda a, b: a + b))
        print(Arrays.stream(arg).reduce(1, lambda a, b: a * b))