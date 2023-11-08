def digit(x, y, z, k):
    return [['x'], ['x', 'x'], ['x', 'x', 'x'], ['x', 'y'], ['y'], ['y', 'x'], 
            ['y', 'x', 'x'], ['y', 'x', 'x', 'x'], ['x', 'z']][k-1]

def toRoman(x):
    if x == 0:
        return ""
    elif x < 0:
        raise ValueError("Negative roman numeral")
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
    print(list(map(toRoman, [1999, 25, 944])))

main()