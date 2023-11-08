def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return str(lcs(xs, ys)) + x
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)

print(lcs('thisisatest', 'testing123testing'))