def iprimes2(limit):
    yield 2
    if limit < 3:
        return
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range(((int(limit ** 0.5) - 3) // 2 + 1)):
        if buf[i] is True:
            p = i + i + 3
            s = p * (i + 1) + i
            for j in range(s, len(buf), p):
                buf[j] = False
    for i in range(lmtbf + 1):
        if buf[i] is True:
            yield (i + i + 3)