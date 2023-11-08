def lcs(a, b):
    aLen = len(a)
    bLen = len(b)
    if aLen == 0 or bLen == 0:
        return ""
    elif a[aLen-1] == b[bLen-1]:
        return lcs(a[:aLen-1], b[:bLen-1]) + a[aLen-1]
    else:
        x = lcs(a, b[:bLen-1])
        y = lcs(a[:aLen-1], b)
        return x if len(x) > len(y) else y