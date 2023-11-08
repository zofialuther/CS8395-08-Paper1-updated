def flatten(input_list):
    for element in input_list:
        if isinstance(element, list):
            yield from flatten(element)
        else:
            yield element

lst = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
flattened_lst = list(flatten(lst))
print(flattened_lst)