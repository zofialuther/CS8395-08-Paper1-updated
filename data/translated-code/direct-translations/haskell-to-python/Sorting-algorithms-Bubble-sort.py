def bsort(s):
    def _bsort(s):
        if len(s) < 2:
            return s
        else:
            x, x2, *xs = s
            if x > x2:
                return [x2, *_bsort([x, *xs])]
            else:
                return [x, *_bsort([x2, *xs])]
    
    result = _bsort(s)
    if result == s:
        return result
    else:
        return bsort(result)