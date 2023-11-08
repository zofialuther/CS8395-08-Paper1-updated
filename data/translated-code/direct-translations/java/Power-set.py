def getpowerset(a, n, ps):
    if n < 0:
        return None
    if n == 0:
        if ps is None:
            ps = []
        ps.append(" ")
        return ps
    ps = getpowerset(a, n-1, ps)
    tmp = []
    for s in ps:
        if s == " ":
            tmp.append(str(a[n-1]))
        else:
            tmp.append(s + str(a[n-1]))
    ps.extend(tmp)
    return ps