def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ""
    elif xstr[-1] == ystr[-1]:
        return lcs(xstr[:-1], ystr[:-1]) + xstr[-1]
    else:
        lcs1 = lcs(xstr, ystr[:-1])
        lcs2 = lcs(xstr[:-1], ystr)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2

if __name__ == "__main__":
    import doctest
    doctest.testmod()