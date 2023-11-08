def digit(x, y, z, k):
    array = [[x], [x, x], [x, x, x], [x, y], [y], [y, x], [y, x, x], [y, x, x, x], [x, z]]
    return array[k - 1]

def toRoman(x):
    if x == 0:
        return ""
    elif x < 0:
        print("Negative roman numeral")
    elif x >= 1000:
        return 'M' + toRoman(x - 1000)
    elif x >= 100:
        q, r = divmod(x, 100)
        return digit('C', 'D', 'M', q) + toRoman(r)
    elif x >= 10:
        q, r = divmod(x, 10)
        return digit('X', 'L', 'C', q) + toRoman(r)
    else:
        return digit('I', 'V', 'X', x)

def main():
    print(toRoman(1999))
    print(toRoman(25))
    print(toRoman(944))