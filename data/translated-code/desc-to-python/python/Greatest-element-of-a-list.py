from functools import reduce

mylist = [12, 45, 67, 23, 102, 78, 34]
max_value = reduce(lambda x, y: x if x > y else y, mylist)
print(max_value)