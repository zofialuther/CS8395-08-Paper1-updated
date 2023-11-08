def permut_Prolog(list1, list2):
    if len(list1) != len(list2):
        return False
    if len(list1) == 0 and len(list2) == 0:
        return True
    else:
        for i in range(len(list2)):
            if list1[0] == list2[i]:
                return permut_Prolog(list1[1:], list2[:i] + list2[i+1:])
        return False