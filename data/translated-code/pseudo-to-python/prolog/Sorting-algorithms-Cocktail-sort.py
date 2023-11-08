def ctail(direction, lst, In, Rev, Flag):
    if direction == 'fwrd' and len(lst) >= 2:
        if lst[0] > lst[1]:
            temp = lst[0]
            lst[0] = lst[1]
            lst[1] = temp
            return ctail('fwrd', lst, In, Rev, Flag)
    elif direction == 'bkwd' and len(lst) >= 2:
        if lst[0] < lst[1]:
            temp = lst[0]
            lst[0] = lst[1]
            lst[1] = temp
            return ctail('bkwd', lst, In, Rev, Flag)
    In.append(lst[0])
    return ctail(direction, lst[1:], In, Rev, Flag)

def cocktailSort(In, Out):
    ctail('fwrd', In, [], [], 'unsorted')
    if Flag == 'sorted':
        Out.append(Rev[0])
        reverse(Rev[1:], Out)
    else:
        ctail('bkwd', Rev, [Rev[0]], [], SortFlag)
        if SortFlag == 'sorted':
            Out.append(Tmp)
        else:
            cocktailSort(Tmp, Out)

def test():
    In = [8, 9, 1, 3, 4, 2, 6, 5, 4]
    print('input =', In)
    R = []
    cocktailSort(In, R)
    print('->', R)