def remFirst(s):
    if len(s) < 1:
        return ""
    else:
        return s[1:]

def remLast(s):
    if len(s) < 1:
        return ""
    else:
        return s[:-1]

def remBoth(s):
    if len(s) < 2:
        return ""
    else:
        return remLast(s[1:])

def main():
    s = "Some string."
    for f in [remFirst, remLast, remBoth]:
        print(f(s))

main()