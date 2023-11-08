def multisplit(LSep, T):
    if LSep == '':
        return [], []
    
    def next_sep(sep_list, string, lst, token, sep, t1):
        if sep_list == []: # if we can't find any separator, the game is over
            if lst == []:
                token = string
                sep = ''
                t1 = ''
            else:
                sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
                sep = sorted_lst[0][2]
                token = ''.join(string.split(sep)[0])
                t1 = string.replace(token + sep, '', 1)
        else:
            hs = sep_list[0]
            sub = string.find(hs)
            if sub != -1:
                lst.append((sub, len(hs), hs))
                next_sep(sep_list[1:], string, lst, token, sep, t1)

    def my_sort(x, y):
        if x[0] < y[0]:
            return -1
        elif x[0] > y[0]:
            return 1
        elif x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            return 0

    def sort_lst(lst):
        return sorted(lst, key=lambda x: (x[0], x[1]))

    next_sep(LSep, T, [], '', '', '')
    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)

    return sort_lst(lst)