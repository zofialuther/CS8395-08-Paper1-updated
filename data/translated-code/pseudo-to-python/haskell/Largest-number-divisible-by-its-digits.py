from Data.Set import fromList
from Numeric import showHex

def lcmDigits(x, y):
    return x * y // gcd(x, y)

allDigits = 0xfedcba987654321
lcmDigits = functools.reduce(lcmDigits, range(1, 16))
upperLimit = allDigits - allDigits % lcmDigits

def main():
    result = [showHex(x, '') for x in range(upperLimit, 0, -lcmDigits) if len(fromList(str(x))) == 15]
    print(result[0])

main()