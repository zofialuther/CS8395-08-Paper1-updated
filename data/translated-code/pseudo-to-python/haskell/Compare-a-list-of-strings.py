def allEq(a):
    if len(a) == 0:
        return True
    else:
        h, t = a[0], a[1:]
        while t and h == t[0]:
            h, t = t[0], t[1:]
    return not t

def allInc(a):
    if len(a) == 0:
        return True
    else:
        h, t = a[0], a[1:]
        while t and h <= t[0]:
            h, t = t[0], t[1:]
    return not t