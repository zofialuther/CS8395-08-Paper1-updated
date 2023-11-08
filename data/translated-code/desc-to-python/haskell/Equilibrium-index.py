def equilibriumIndices(arr):
    from itertools import accumulate
    
    left_sums = list(accumulate(arr))
    right_sums = list(accumulate(reversed(arr)))
    right_sums = list(reversed(right_sums))
    
    result = [i for i, (left, right) in enumerate(zip(left_sums, right_sums)) if left == right]
    
    return result

def main():
    input1 = [-7, 1, 5, 2, -4, 3, 0]
    input2 = [1, 2, 3, 4, 5]
    input3 = [1, 1, 1, 1, 1, 1]
    
    print(equilibriumIndices(input1))
    print(equilibriumIndices(input2))
    print(equilibriumIndices(input3))

main()