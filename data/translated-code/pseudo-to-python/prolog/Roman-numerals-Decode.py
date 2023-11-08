def decode_digit(i, n):
    if i == "i":
        return 1
    elif i == "v":
        return 5
    elif i == "x":
        return 10
    elif i == "l":
        return 50
    elif i == "c":
        return 100
    elif i == "d":
        return 500
    elif i == "m":
        return 1000

def decode_string(Sum, LastValue, String, NextSum):
    if len(String) == 0:
        return Sum
    else:
        Digit = String[0]
        Rest = String[1:]
        Value = decode_digit(Digit, 0)
        if Value < LastValue:
            Sum = LastValue - Value
        else:
            Sum = LastValue + Value
        return decode_string(Sum, Value, Rest, NextSum)

def decode(Atom):
    String = list(Atom)
    String.reverse()
    Last = String[0]
    Rest = String[1:]
    Start = decode_digit(Last, 1)
    return decode_string(Start, Start, Rest, 0)

def test():
    print(decode("mcmxc"))  # 1990
    print(decode("mmviii"))  # 2008
    print(decode("mdclxvi"))  # 1666