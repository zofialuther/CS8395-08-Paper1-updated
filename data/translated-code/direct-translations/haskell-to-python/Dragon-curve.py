def x(n):
    if n == 0:
        return ""
    else:
        return x(n-1) + " +" + y(n-1) + " f +"

def y(n):
    if n == 0:
        return ""
    else:
        return " - f" + x(n-1) + " -" + y(n-1)

def dragon(n):
    return "0 setlinewidth 300 400 moveto" + "/f{2 0 rlineto}def/+{90 rotate}def/-{-90 rotate}def\n" + "f" + x(n) + " stroke showpage"

print(dragon(14))