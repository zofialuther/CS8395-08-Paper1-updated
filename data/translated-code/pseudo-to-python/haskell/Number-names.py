def spellInteger(n):
    if n < 0:
        return "negative " + spellInteger(-n)
    elif n < 20:
        return small(n)
    elif n < 100:
        a, b = divmod(n, 10)
        return tens(a) + nonzero('-', b)
    elif n < 1000:
        a, b = divmod(n, 100)
        return small(a) + " hundred" + nonzero(' ', b)
    else:
        return ", ".join(map(big, reversed([x for x in range(0, len(str(n)), 3)]), unfoldr(uff, n)))

def nonzero(c, n):
    if n == 0:
        return ""
    else:
        return c + spellInteger(n)

def uff(n):
    if n == 0:
        return None
    else:
        return (uncurry(flip, divmod(n, 1000)))

def small(n):
    return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][int(n)]

def tens(n):
    return [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][int(n)]

def big(e, n):
    if e == 0:
        return spellInteger(n)
    elif e == 1:
        return spellInteger(n) + " thousand"
    else:
        return spellInteger(n) + ' ' + l[e] + "illion"