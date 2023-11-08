def concatenate_lists(list1, list2):
    if not list1:
        return list2
    else:
        list2.append(list1[0])
        return concatenate_lists(list1[1:], list2)