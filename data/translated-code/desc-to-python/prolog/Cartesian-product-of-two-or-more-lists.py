def product(list1, list2):
    if not list1:
        return []
    else:
        return [(list1[0], x) for x in list2] + product(list1[1:], list2)