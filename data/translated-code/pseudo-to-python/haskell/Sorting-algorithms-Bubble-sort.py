def bsort(s):
    t = _bsort(s)
    if t == s:
        return t
    else:
        return bsort(t)

def _bsort(s):
    if len(s) <= 1:
        return s
    else:
        for i in range(len(s) - 1):
            if s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
        return _bsort(s)