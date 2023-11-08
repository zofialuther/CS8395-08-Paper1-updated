mylist = [47, 11, 42, 102, 13]
max_value = reduce(lambda a, b: a if (a > b) else b, mylist)
print(max_value)