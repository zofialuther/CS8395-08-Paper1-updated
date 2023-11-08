def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x = xstr[0]
    xs = xstr[1:]
    y = ystr[0]
    ys = ystr[1:]
    if x == y:
        return lcs(xs, ys) + x
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)