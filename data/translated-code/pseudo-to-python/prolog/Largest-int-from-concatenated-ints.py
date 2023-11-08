def largest_int_v2(In, Out):
    LC = list(map(name, In))
    LCS = sorted(LC, key=my_sort)
    LC1 = LCS + LC
    Out = name(LC1)

def my_sort(L1, L2):
    V1 = L1 + L2
    I1 = name(V1)
    V2 = L2 + L1
    I2 = name(V2)
    if I1 < I2:
        return -1
    elif I1 == I2:
        return 0
    else:
        return 1

def my_sort(R, L1, L2):
    if L1[0] > L2[0]:
        return 1
    elif L1[0] < L2[0]:
        return -1
    else:
        if len(L1) > 1:
            return my_sort(R, L1[1:], L2)
        elif len(L2) > 1:
            return my_sort(R, L1, L2[1:])
        else:
            return 0