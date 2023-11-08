def remFirst(s):
    if s == "":
        return ""
    else:
        return s[1:]

def remLast(s):
    if s == "":
        return ""
    else:
        return s[:-1]

def remBoth(s):
    if s == "":
        return ""
    else:
        return s[1:-1]

s = "Some string."
for f in [remFirst, remLast, remBoth]:
    print(f(s))