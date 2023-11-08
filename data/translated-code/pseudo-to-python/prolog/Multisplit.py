def multisplit(LSep, T):
    if not T:
        return []
    else:
        result = []
        Token, Sep, T1 = find_next_sep(LSep, T, [], '', '', '')
        if Token:
            result.append(Token)
        if Sep:
            result.append(Sep)
        return result + multisplit(LSep, T1)

def find_next_sep(LSep, T, Lst, Token, Sep, T1):
    if not Lst:
        Token = T
        Sep = ''
        T1 = ''
    else:
        Lst.sort(key=lambda x: len(x[2]), reverse=True)
        pos, length, sep = Lst[0]
        Token = T[:pos]
        Tmp = Token + sep
        T1 = Tmp + T[pos+length:]

def find_next_sep(LSep, T, Lst, Token, Sep, T1):
    if LSep:
        HSep = LSep[0]
        pos, length = T.find(HSep), len(HSep)
        if pos != -1:
            Lst.append((pos, length, HSep))
        find_next_sep(LSep[1:], T, Lst, Token, Sep, T1)
    else:
        find_next_sep(LSep[1:], T, Lst, Token, Sep, T1)

def my_sort(N1, N2):
    if N1 < N2:
        return -1
    elif N1 > N2:
        return 1
    else:
        return 0