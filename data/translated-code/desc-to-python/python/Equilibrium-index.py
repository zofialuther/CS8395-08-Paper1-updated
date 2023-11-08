def eqindexMultiPass(arr):
    return [i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i+1:])]

input_list = [1, 2, 3, 4, 5, 5, 2, 1]
result = eqindexMultiPass(input_list)
print(result)