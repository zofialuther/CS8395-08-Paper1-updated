def concatenateList(list1, list2):
    if not list1:
        return list2
    else:
        return [list1[0]] + concatenateList(list1[1:], list2)