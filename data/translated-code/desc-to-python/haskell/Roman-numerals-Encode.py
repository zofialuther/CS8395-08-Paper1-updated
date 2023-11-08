def digit(x, y, z, k):
    if k == 0:
        return ""
    elif k < 4:
        return x + digit(x, y, z, k-1)
    elif k == 4:
        return x + y
    elif k < 9:
        return y + digit(x, y, z, k-5)
    else:
        return x + z

def toRoman(x):
    if x < 1:
        return ""
    elif x < 4:
        return "I" + toRoman(x-1)
    elif x == 4:
        return "IV"
    elif x < 9:
        return "V" + toRoman(x-5)
    elif x == 9:
        return "IX"
    elif x < 40:
        return "X" + toRoman(x-10)
    elif x < 50:
        return "XL" + toRoman(x-40)
    elif x < 90:
        return "L" + toRoman(x-50)
    elif x < 100:
        return "XC" + toRoman(x-90)
    elif x < 400:
        return "C" + toRoman(x-100)
    elif x < 500:
        return "CD" + toRoman(x-400)
    elif x < 900:
        return "D" + toRoman(x-500)
    elif x < 1000:
        return "CM" + toRoman(x-900)
    else:
        return "M" + toRoman(x-1000)

def main():
    numbers = [3, 7, 14, 21, 36, 49, 88, 99, 444, 999, 1000]
    for num in numbers:
        print(num, ":", toRoman(num))

main()