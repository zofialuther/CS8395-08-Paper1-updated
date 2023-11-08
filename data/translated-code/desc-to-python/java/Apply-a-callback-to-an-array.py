class ArrayCallback:
    def main(self):
        arr = [1, 2, 3, 4, 5]
        result = map(lambda x: x ** 3, arr)
        print(list(result))
        sum_cubes = reduce(lambda x, y: x + y, result)
        print(sum_cubes)