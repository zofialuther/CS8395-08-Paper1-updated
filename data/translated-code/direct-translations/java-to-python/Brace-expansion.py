def main():
    strings = ["It{{em,alic}iz,erat}e{d,}, please.",
               "~/{Downloads,Pictures}/*.{jpg,gif,png}",
               "{,{,gotta have{ ,\\, again\\, }}more }cowbell!",
               "{}} some }{,{\\\\{ edge, edge} \\,}{ cases, {here} \\\\\\\\\\}"]
    
    for s in strings:
        print()
        expand(s)

def expand(s):
    expandR("", s, "")

def expandR(pre, s, suf):
    i1 = -1
    i2 = 0
    noEscape = s.replace("([\\\\]{2}|[\\\\][,}{])", "  ")
    sb = None
    
    while (i1 := noEscape.find('{', i1 + 1)) != -1:
        i2 = i1 + 1
        sb = list(s)
        depth = 1
        for i in range(i2, len(s)):
            c = noEscape[i]
            if c == '{':
                depth += 1
            if c == '}':
                depth -= 1
            if c == ',' and depth == 1:
                sb[i] = '\u0000'
            elif c == '}' and depth == 0 and '\u0000' in sb:
                break

    if i1 == -1:
        if len(suf) > 0:
            expandR(pre + s, suf, "")
        else:
            print(f"{pre}{s}{suf}")
    else:
        for m in ''.join(sb[i1 + 1:i2]).split('\u0000'):
            expandR(pre + s[:i1], m, s[i2 + 1:] + suf)

main()