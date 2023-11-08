def equilibriumIndices(xs):
    return [i for i, (left_sum, right_sum) in enumerate(zip(scanl1(lambda x, y: x + y, xs), scanr1(lambda x, y: x + y, xs))) if left_sum == right_sum]

# TEST
def main():
    inputs = [[-7, 1, 5, 2, -4, 3, 0],
              [2, 4, 6],
              [2, 9, 2],
              [1, -1, 1, -1, 1, -1, 1],
              [1],
              []]
    for input in inputs:
        print(equilibriumIndices(input))

main()