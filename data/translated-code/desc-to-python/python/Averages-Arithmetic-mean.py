def average(nums):
    total = sum(nums)
    return total / len(nums)

list1 = [0, 0, 0, 0, 5, 0, 0, 0, 3, 0]
list2 = [1000000000, 0.000001, 0.0000001, 10000000000, 0.00000001]

result1 = average(list1)
result2 = average(list2)

print(result1)
print(result2)