def printVerse(name):
    sb = name.lower()
    sb = sb[0].upper() + sb[1:]
    x = sb
    if x[0] in ['a', 'e', 'i', 'o', 'u']:
        y = x.lower()
    else:
        y = x[1:]
    b = "b" + y
    f = "f" + y
    m = "m" + y
    if x[0] == 'B':
        b = y
    elif x[0] == 'F':
        f = y
    elif x[0] == 'M':
        m = y
    print("%s, %s, bo-%s" % (x, x, b))
    print("Banana-fana fo-%s" % f)
    print("Fee-fi-mo-%s" % m)
    print("%s!" % x)

def main(args):
    names = ["Gary", "Earl", "Billy", "Felix", "Mary", "Steve"]
    for name in names:
        printVerse(name)