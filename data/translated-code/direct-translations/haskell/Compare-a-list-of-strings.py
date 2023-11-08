def allEq(lst):
    if len(lst) == 0:
        return True
    else:
        return not any(x != lst[0] for x in lst)

def allInc(lst):
    if len(lst) == 0:
        return True
    else:
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))