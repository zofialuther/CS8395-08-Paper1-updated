def main():
    for s in ["It{{em,alic}iz,erat}e{d,}, please.",
              "~/{Downloads,Pictures}/*.{jpg,gif,png}",
              "{,{,gotta have{ ,\\, again\\, }}more }cowbell!",
              "{}} some }{,{\\\\{ edge, edge} \\,}{ cases, {here} \\\\\\\\\\}"]:
        print(expand(s))

def expand(s):
    expandR("", s, "")

def expandR(pre, s, suf):
    i1 = -1
    i2 = 0
    noEscape = s.replace("([\\\\]{2}|[\\\\][,}{])", "  ")
    sb = None

    while (i1 = noEscape.find('{', i1 + 1)) != -1:
        i2 = i1 + 1
        sb = StringBuilder(s)
        depth = 1
        for c in s[i2:]:
            if c == '{':
                depth = depth + 1
            if c == '}':
                depth = depth - 1
            if c == ',' and depth == 1:
                sb.setCharAt(i2, '\u0000')
            if c == '}' and depth == 0 and sb.indexOf("\u0000") != -1:
                break

    if i1 == -1:
        if len(suf) > 0:
            expandR(pre + s, suf, "")
        else:
            print(pre + s + suf)
    else:
        for m in sb.substring(i1 + 1, i2).split("\u0000", -1):
            expandR(pre + s[:i1], m, s[i2 + 1:] + suf)