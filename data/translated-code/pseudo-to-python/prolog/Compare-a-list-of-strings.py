def lexically_equal(S1, S2, S3):
    # code for comparing if three elements are lexically equal
    pass

def in_order(G1, L, G2):
    # code for comparing if the second element is less than the first element
    pass

def test_list(List):
    L = List[0]
    print('for list ', List)
    if foldl(lexically_equal, T, L, _):
        print('The items in the list ARE lexically equal')
    else:
        print('The items in the list are NOT lexically equal')
    if foldl(in_order, T, L, _):
        print('The items in the list ARE in ascending order')
    else:
        print('The items in the list are NOT in ascending order')
    print()

def test():
    for List in los:
        test_list(List)