def lexically_equal(lst):
    return all(lst[i] == lst[i+1] for i in range(len(lst)-1))

def ascending_order(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def test_list(lst):
    if lexically_equal(lst) and ascending_order(lst):
        print(f"{lst} is lexically equal and in ascending order")
    else:
        print(f"{lst} is not lexically equal and in ascending order")

def los(lists):
    for lst in lists:
        test_list(lst)