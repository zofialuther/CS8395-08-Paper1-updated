def maxnum(nums):
    nums = [str(x) for x in nums]
    nums.sort(key=lambda x: x*3, reverse=True)
    return int(''.join(nums))

num_tuples = [(3, 30, 34, 5), (1, 2, 3, 4, 5), (9, 99, 999)]
for tup in num_tuples:
    print("Original numbers:", tup)
    print("Largest integer:", maxnum(tup))