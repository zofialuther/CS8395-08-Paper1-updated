def lexically_equal(s1, s2, s3):
    return s1 == s2 == s3

def in_order(g, l, g):
    return l < g

def test_list(lst):
    L = lst[0]
    print('for list', lst)
    if all(lexically_equal(x, L, _) for x in lst[1:]):
        print('The items in the list ARE lexically equal')
    else:
        print('The items in the list are NOT lexically equal')
    
    if all(in_order(x, L, _) for x in lst[1:]):
        print('The items in the list ARE in ascending order')
    else:
        print('The items in the list are NOT in ascending order')
    
    print()

def test():
    for lst in [["AA","BB","CC"],["AA","AA","AA"],["AA","CC","BB"],["AA","ACB","BB","CC"],["single_element"]]:
        test_list(lst)

test()