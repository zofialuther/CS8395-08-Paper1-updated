def max_list(L, V):
    R = [x for x in L if x != V]
    for x in R:
        if x > V:
            return False
    return True