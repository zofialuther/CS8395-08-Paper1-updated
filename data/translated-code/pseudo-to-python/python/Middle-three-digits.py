def mid3digits(n):
    m = abs(n)
    s = str(m)
    if m < 100:
        return "Less than 3 digits"
    elif len(s) % 2 == 0:
        return "Even digit count"
    else:
        return s[len(s)//2 - 1 : len(s)//2 + 2]