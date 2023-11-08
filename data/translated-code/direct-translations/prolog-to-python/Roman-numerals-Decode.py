def decode_digit(i, 1):
    return i

def decode_digit(v, 5):
    return v

def decode_digit(x, 10):
    return x

def decode_digit(l, 50):
    return l

def decode_digit(c, 100):
    return c

def decode_digit(d, 500):
    return d

def decode_digit(m, 1000):
    return m

def decode_string(Sum, _, digits, Sum):
    return Sum

def decode_string(LastSum, LastValue, digits, NextSum):
    if not digits:
        return NextSum
    
    digit = digits[0]
    rest = digits[1:]
    
    value = decode_digit(digit)
    
    if value < LastValue:
        Sum = LastSum - value
        return decode_string(Sum, value, rest, NextSum)
    else:
        Sum = LastSum + value
        return decode_string(Sum, value, rest, NextSum)

def decode_string(Atom, Value):
    String = list(Atom)
    Last = String[-1]
    Rest = String[:-1]
    Start = decode_digit(Last)
    return decode_string(Start, Start, Rest, Value)

def test():
    decode_string("mcmxc", 1990)
    decode_string("mmviii", 2008)
    decode_string("mdclxvi", 1666)